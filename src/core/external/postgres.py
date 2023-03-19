from typing import Annotated, AsyncGenerator

from fastapi import Depends
from loguru import logger
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.api.models.common import Base

from ..settings.db_settings import settings


class Engine:
    def __init__(self):
        self.engine = create_async_engine(
            url=settings.get_pg_url(),
            pool_size=1,
            pool_recycle=3600,
            connect_args={"server_settings": {"jit": "off"}},
            echo=True,
        )

        self.session = async_sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False  # type: ignore
        )


engine = Engine()


async def create_db_and_tables():
    async with engine.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Tables were created!")


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with engine.session() as session:
        yield session


AnnotatedSession = Annotated[AsyncSession, Depends(get_session)]

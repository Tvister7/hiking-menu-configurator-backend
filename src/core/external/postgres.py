from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from ..settings import settings


class Engine:
    def __init__(self):

        self.engine = create_async_engine(
            url=settings.postgres_url,
            pool_size=1,
            pool_recycle=3600,
            connect_args={"server_settings": {"jit": "off"}},
            echo=True,
        )

        self.session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False  # type: ignore
        )

    async def _create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
            logger.info("Tables were created!")


engine = Engine()

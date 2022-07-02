from loguru import logger

# from sqlalchemy.exc import NoResultFound
from sqlmodel import select

from ..api.models.meal import Meal
from .postgres import engine


class DatabaseActions:
    @staticmethod
    async def get_all_meals_from_postgres() -> list[Meal]:
        async with engine.session() as session:
            stmt = select(Meal)
            result = await session.execute(stmt)
            logger.info("Got wm info from postgres")
            tuple_res = result.one()[0]
            return tuple_res

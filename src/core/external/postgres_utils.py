from loguru import logger
from sqlalchemy import select

from ..api.models.meals.db_meal import DBMeal
from ..api.models.meals.meal import Meal
from .postgres import engine

# from sqlalchemy.exc import NoResultFound


class DatabaseActions:
    @staticmethod
    async def get_all_meals_from_postgres() -> list[Meal]:
        async with engine.session() as session:
            stmt = select(DBMeal)
            res = await session.execute(stmt)
            logger.info("Got wm info from postgres")
            result = res.fetchall()
            pydantic_object = [Meal.from_orm(el) for el in result]
            return pydantic_object

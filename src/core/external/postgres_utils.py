from loguru import logger
from sqlalchemy import select

from core.api.models.users.db_user import DBUser
from core.api.models.users.user import User

from ..api.models.meals.db_meal import DBMeal
from ..api.models.meals.meal import Meal
from .postgres import engine

# from sqlalchemy.exc import NoResultFound


class DBActionsMeals:
    @staticmethod
    async def get_all_meals_from_relational_db() -> list[Meal]:
        async with engine.session() as session:
            stmt = select(DBMeal)
            res = await session.execute(stmt)
            logger.info("Got wm info from db")
            result = res.fetchall()
            pydantic_object = [Meal.from_orm(el) for el in result]
            return pydantic_object


class DBActionsUsers:
    @staticmethod
    async def get_all_users_from_relational_db() -> list[User]:
        async with engine.session() as session:
            stmt = select(DBUser)
            res = await session.execute(stmt)
            logger.info("Got wm info from db")
            result = res.fetchall()
            pydantic_object = [User.from_orm(el) for el in result]
            return pydantic_object

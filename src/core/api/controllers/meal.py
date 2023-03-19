from sqlalchemy.ext.asyncio import AsyncSession

from ...external.postgres_utils import DBActionsMeals
from ..models.meals.meal import Meal


async def get_all_meals_controller(session: AsyncSession) -> list[Meal]:
    return await DBActionsMeals.get_all_meals_from_relational_db(session)

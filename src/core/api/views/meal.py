# from fastapi.param_functions import Depends  # noqa
from fastapi.routing import APIRouter

from core.api.models.meals.meal import Meal

from ..controllers.meal import get_all_meals_controller

meal_router = APIRouter(tags=["base"])


@meal_router.get("/get_meals")
async def get_all_meals() -> list[Meal]:
    return await get_all_meals_controller()

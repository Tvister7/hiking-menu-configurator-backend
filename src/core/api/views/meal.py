from fastapi.routing import APIRouter

from core.api.models.meals.meal import Meal
from core.external.postgres import AnnotatedSession

from ..controllers.meal import get_all_meals_controller

meal_router = APIRouter(tags=["base"])


@meal_router.get("/get_meals")
async def get_all_meals(session: AnnotatedSession) -> list[Meal]:
    return await get_all_meals_controller(session)

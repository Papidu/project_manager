from fastapi import APIRouter

from .projects.views import router as project_router
from .tasks.views import router as task_router

router = APIRouter()
router.include_router(router=project_router, prefix="/products")
router.include_router(router=task_router, prefix="/tasks")

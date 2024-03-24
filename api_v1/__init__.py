from fastapi import APIRouter

from .projects.views import router as project_router
from .tasks.views import router as tasks_router

router = APIRouter()
router.include_router(project_router, prefix="/project")
router.include_router(tasks_router, prefix="/tasks")

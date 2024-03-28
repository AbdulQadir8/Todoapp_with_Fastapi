from fastapi import APIRouter, Depends

# from api.auth import authent
from public.project import view  as projects
from public.todo import view as todos
from public.user import view as users

api = APIRouter()

api.include_router(
    projects.router,
    prefix="/projects",
    tags=["Projects"],
    )

api.include_router(
    todos.router,
    prefix="/todos",
    tags=["Todos"],
    )

api.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
    )
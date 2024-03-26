from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from typing import Annotated

from database import get_dep
from public.project.crud import (
    create_project,
    get_project,
    get_projects,
    update_project, 
    delete_project)

from public.project.models import CreateProject,ProjectResponse,ProjectResponse, ProjectUpdate

router = APIRouter()

@router.post("/",response_model=ProjectResponse)
def create_a_project(project: CreateProject, session= Annotated[Session, Depends(get_dep)]):
    return create_project(project=project,session=session)

@router.get("/",response_model=ProjectResponse)
def get_a_project(id: int, session= Annotated[Session, Depends(get_dep)]):
    return get_project(id=id, session=session)

@router.get("/",response_model=list[ProjectResponse])
def get_projects(offset: int=0,
                 limit: int =Query(default=100,lte=100),
                 session= Annotated[Session, Depends(get_dep)]):
        return get_projects(session)

@router.patch("/",response_model=ProjectResponse)
def update_a_project(id: int,project: ProjectUpdate, session= Annotated[Session, Depends(get_dep)]):
     return update_project(id=id,project=project,session=session)

@router.delete("/")
def delete_a_proejct(id: int, session= Annotated[Session, Depends(get_dep)]):
     return delete_project(id=id,session=session)









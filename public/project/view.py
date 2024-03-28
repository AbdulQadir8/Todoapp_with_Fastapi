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
def create_a_project(project: CreateProject, session: Session = Depends(get_dep)):
    return create_project(project=project,session=session)

@router.get("/{project_id}",response_model=ProjectResponse)
def get_a_project(project_id: int, session: Session = Depends(get_dep)):
    return get_project(id=project_id, session=session)

@router.get("/",response_model=list[ProjectResponse])
def get_all_projects(offset: int=0,
                 limit: int =Query(default=100,lte=100),
                 session: Session = Depends(get_dep)):
        return get_projects(offset=offset,limit=limit,session=session)

@router.patch("/{project_id}",response_model=ProjectResponse)
def update_a_project(project_id: int,project_data: ProjectUpdate, session: Session = Depends(get_dep)):
     return update_project(id=project_id,project_data=project_data,session=session)

@router.delete("/{project_id}")
def delete_a_proejct(project_id: int, session: Session = Depends(get_dep)):
     return delete_project(id=project_id,session=session)









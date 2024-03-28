from public.project.models  import Project, CreateProject, ProjectUpdate, ProjectResponse
from fastapi import  Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Annotated
from database import get_dep

def get_project(id: int, session: Session = Depends(get_dep)):
    project = session.get(Project,id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project not found with ID:{id}")
    
    return project

def get_projects(offset: int=0,limit: int=20,session: Session = Depends(get_dep)):
    statement = select(Project).offset(offset).limit(limit)
    projects = session.exec(statement).all()
    return projects


def create_project(project: CreateProject, session: Session = Depends(get_dep)):
    project_to_add = Project.model_validate(project)
    session.add(project_to_add)
    session.commit()
    session.refresh(project_to_add)
    return project_to_add

def update_project(id: int, project_data: ProjectUpdate, session: Session = Depends(get_dep)):
    project_to_update = session.get(Project, id)
    if not project_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project not found with ID:{id}")
    project_dict_data = project_data.model_dump(exclude_unset=True)
    for key, value in project_dict_data.items():
        setattr(project_to_update,key,value)

    session.add(project_to_update)
    session.commit()
    session.refresh(project_to_update)
    return project_to_update

def delete_project(id: int, session: Session = Depends(get_dep)):
    project_to_delete = session.get(Project,id)
    if not project_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Project not found with :ID:{id}")
    
    session.delete(project_to_delete)
    session.commit()
    return {"Message":"Project Deleted"}
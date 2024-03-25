from model import Todo, TodoCreate, TodoUpdate, TodoResponse
from fastapi import  Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Annotated
from database import get_dep





def get_todo(id: int, session: Annotated[Session, Depends(get_dep)]):
    todo = session.get(Todo,id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo not found with id:{id}"
        )
    return todo


def get_todos(session: Annotated[Session, Depends(get_dep)]):
    statement = select(Todo)
    todos = session.exec(statement).all()
    return todos

def create_todo(todo: TodoCreate, session: Annotated[Session, Depends(get_dep)]):
    todo_to_db = Todo.model_validate(todo)
    session.add(todo_to_db)
    session.commit()
    session.refresh(todo_to_db)
    return todo_to_db


def update_todo(id: int, todo_data: TodoUpdate, session: Annotated[Session, Depends(get_dep)]):
    todo_to_update = session.get(Todo,id)
    if not todo_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo not found with id:{id}")
    todo_dict_data = todo_data.model_dump(exclude_unset=True)
    for key, value in todo_dict_data.items():
        setattr(todo_to_update, key, value)

    session.add(todo_to_update)
    session.commit()
    session.refresh(todo_to_update)
    return todo_to_update

def delete_todo(id: int, session: Annotated[Session, Depends(get_dep)]):
    todo_to_delete = session.get(Todo,id)
    if not todo_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Todo not found with id:{id}"
                            )
    session.delete(todo_to_delete)
    session.commit()
    return {"ok":"True"}


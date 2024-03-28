from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from typing import Annotated

from database import get_dep
from public.todo.crud import (
    create_todo,
    get_todo,
    get_todos,
    update_todo,
    delete_todo
)

from public.todo.models import TodoCreate, TodoResponse, TodoUpdate, Todo

router = APIRouter()

@router.post("/", response_model=TodoResponse)
def create_a_todo(todo: TodoCreate, session:Session = Depends(get_dep)):
    return create_todo(todo=todo,session=session)

@router.get("/{todo_id}", response_model=TodoResponse)
def get_a_todo(todo_id: int, session:Session = Depends(get_dep)):
    return get_todo(id=todo_id, session=session)

@router.get("/", response_model=list[TodoResponse])
def get_all_todos(
    offset: int = 0,
    limit: int= Query(default=100,lte=100),
    session: Session = Depends(get_dep)):

    return get_todos(offset=offset,limit=limit,session=session)

@router.patch("/{todo_id}", response_model=TodoResponse)
def update_a_todo(todo_id: int,todo_data: TodoUpdate, session:Session = Depends(get_dep)):
    return update_todo(id=todo_id,todo_data=todo_data, session=session)

@router.delete("/{todo_id}")
def delete_a_todo(todo_id: int, session:Session = Depends(get_dep)):
    return delete_todo(id=todo_id, session=session)


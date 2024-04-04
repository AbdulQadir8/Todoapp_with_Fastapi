from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from typing import Annotated

from database import get_dep
from public.user.crud import (get_user,
                              get_users,
                              create_user, 
                              update_user, 
                              delete_user)
from public.model.models import UserCreate,UserResponse,UserUpdate,User

router = APIRouter()

@router.post("/",response_model=UserResponse)
def create_a_user(user: UserCreate, session: Session = Depends(get_dep)):
    return create_user(user=user,session=session)

@router.get("/{user_id}",response_model=UserResponse)
def get_a_user(user_id: int, session: Session = Depends(get_dep)):
    return get_user(id=user_id, session=session)

@router.get("/", response_model=list[UserResponse])
def get_all_users(offset: int=0,
                  limit=Query(default=100,lte=100),
                  session: Session = Depends(get_dep)):
    return get_users(offset=offset,limit=limit,session=session)

@router.patch("/{user_id}",response_model=UserResponse)
def update_a_user(user_id: int,user_data: UserUpdate, session: Session = Depends(get_dep)):
    return update_user(id=user_id,user_data=user_data,session=session)

@router.delete("/{user_id}")
def delete_a_user(user_id: int, session: Session = Depends(get_dep)):
    return delete_user(id=user_id, session=session)

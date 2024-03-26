from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from typing import Annotated

from database import get_dep
from public.user.crud import (get_user,
                              get_users,
                              create_user, 
                              update_user, 
                              delete_user)
from public.user.models import UserCreate,UserResponse,UserUpdate,User

router = APIRouter()

@router.get("/",response_model=UserResponse)
def get_a_user(id: int, session= Annotated(Session, Depends(get_dep))):
    return get_user(id=id, session=session)

@router.get("/", response_model=list[UserResponse])
def get_users(offset: int=0,
              limit=Query(default=100,lte=100),
              session= Annotated[Session, Depends(get_dep)]):
    return get_users(offset=offset,limit=limit,session=session)

@router.patch("/",response_model=UserResponse)
def create_a_user(id: int,user_data: UserCreate, session= Annotated[Session, Depends(get_dep)]):
    return create_user(id=id,user_data=user_data,session=session)

@router.delete("/")
def delete_a_user(id: int, session = Annotated[Session, Depends(get_dep)]):
    return delete_user(id=id, session=session)

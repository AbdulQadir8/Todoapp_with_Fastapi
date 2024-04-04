from public.model.models import UserCreate, UserResponse, User, UserUpdate
from typing import Annotated
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from database import get_dep



def get_user(id: int, session: Session = Depends(get_dep)):
        user = session.get(User,id)
        if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found with ID:{id}")
        
        return user

def get_users(offset: int=0,limit: int=20,session: Session = Depends(get_dep)):
        statement = select(User).offset(offset).limit(limit)
        users = session.exec(statement).all()
        return users

def create_user(user: UserCreate, session: Session = Depends(get_dep)):    
                user_to_db = User.model_validate(user)
                session.add(user_to_db)
                session.commit()
                session.refresh(user_to_db)
                return user_to_db


def update_user(id: int,user_data: UserUpdate, session: Session = Depends(get_dep)):
        user_to_update = session.get(User,id)
        if not user_to_update:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                     detail=f"User not found with ID:{id}")
        user_dict_data = user_data.model_dump(exclude_unset=True)
        for key, value in user_dict_data.items():
                setattr(user_to_update, key, value)

        session.add(user_to_update)
        session.commit()
        session.refresh(user_to_update)
        return user_to_update


def delete_user(id: int, session: Session = Depends(get_dep)):
        todo_to_delete = session.get(User,id)
        if not todo_to_delete:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"If user not found ID:{id}")
        session.delete(todo_to_delete)
        session.commit()
        return {"Message":"User deleted"}
        
        



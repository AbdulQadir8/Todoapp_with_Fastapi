from sqlmodel import SQLModel, Field
from datetime import datetime, timezone



class Todo(SQLModel, table=True):
    id: int|None = Field(default=None,primary_key=True)
    name: str = Field(index=True)
    body: str 
    status: str
    due_date: datetime

class TodoCreate(SQLModel):
    name: str
    body: str
    status: str
    due_date: datetime


class TodoResponse(SQLModel):
    id: int
    name: str
    body: str
    status: str
    due_date: datetime


class TodoUpdate(SQLModel):
    name: str | None = None
    body: str | None = None
    status: str | None = None
    due_date: datetime | None = None


class User(SQLModel, table=True):
    id: int | None = Field(default=None,primary_key=True)
    user_name: str = Field(index=True)
    user_email: str 
    user_password: str
    birthday: datetime
    phone_number: int
    time_stamp: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})


class UserCreate(SQLModel):
    user_name: str
    user_email: str
    user_password: str
    birthday: datetime
    phone_number: int
    time_stamp: datetime


class UserResponse(SQLModel):
    id: int
    user_name: str
    user_email: str
    user_password: str
    birthday: datetime
    phone_number: int
    time_stamp: datetime

class UserUpdate(SQLModel):
    user_name: str
    user_email: str
    user_password: str
    birthday: datetime
    phone_number: int
    time_stamp: datetime




     
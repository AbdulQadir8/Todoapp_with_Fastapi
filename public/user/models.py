from sqlmodel import SQLModel, Field
from datetime import datetime, timezone





class User(SQLModel, table=True):
    id: int | None = Field(default=None,primary_key=True)
    user_name: str = Field(index=True)
    user_email: str 
    user_password: str
    birthday: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})
    phone_number: str
    time_stamp: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})


class UserCreate(SQLModel):
    user_name: str
    user_email: str
    user_password: str
    birthday: datetime
    phone_number: str
    time_stamp: datetime


class UserResponse(SQLModel):
    id: int
    user_name: str
    user_email: str
    user_password: str
    birthday: datetime
    phone_number: str
    time_stamp: datetime

class UserUpdate(SQLModel):
    user_name: str | None = None
    user_email: str | None = None
    user_password: str | None = None
    birthday: datetime | None = None
    phone_number: str | None = None
    time_stamp: datetime | None = None
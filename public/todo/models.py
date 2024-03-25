from sqlmodel import SQLModel, Field
from datetime import datetime



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

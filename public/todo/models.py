from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from datetime import datetime, timezone



class Todo(SQLModel, table=True):
    id: int|None = Field(default=None,primary_key=True)
    name: str = Field(index=True)
    body: str 
    status: str
    due_date: datetime
    project_id: int = Relationship(default=None, foreign_key="project.id")
    creater_id: int = Relationship(default=None, foreign_key="user.id")
    assigned_id: int = Relationship(default=None, foreign_key="user.id")
    time_stamp: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})


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

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from public.todo.models import Todo



class Project(SQLModel, table=True):
    id: int = Field(default=None,primary_key=True)
    project_name: str  = Field(index=True)
    status: str = Field(default="undone")
    time_stamp: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})


class CreateProject(SQLModel):
    project_name: str
    status: str
    time_stamp: datetime


class ProjectResponse(SQLModel):
    id: int
    project_name: str
    status: str
    time_stamp: datetime

class ProjectUpdate(SQLModel):
    project_name: str | None = None
    status: str | None = None
    time_stamp: datetime | None = None

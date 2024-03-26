from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone



class Project(SQLModel, table=True):
    id: int = Field(default=None,primary_key=True)
    project_name: str  = Field(index=True)
    status: str = Field(default="undone")
    time_stamp: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})
    creater_id: list[int] = Relationship(default=None, foreign_key="user.id")

class CreateProject(SQLModel):
    project_name: str
    status: str
    time_stamp: datetime
    creater_id: int


class ProjectResponse(SQLModel):
    id: int
    project_name: str
    status: str
    time_stamp: datetime
    creater_id: int

class ProjectUpdate(SQLModel):
    project_name: str
    status: str
    time_stamp: datetime
    creater_id: int
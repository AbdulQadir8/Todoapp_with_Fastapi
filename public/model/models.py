from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from utils.generic_models import UserTodoLink


# User class  Models

class User(SQLModel, table=True):
    id: int | None = Field(default=None,primary_key=True)
    user_name: str = Field(index=True)
    user_email: str 
    user_password: str
    birthday: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})
    phone_number: str
    time_stamp: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})
    todos: list["Todo"] = Relationship(back_populates="users",link_model=UserTodoLink)


class UserCreate(SQLModel):
    user_name: str
    user_email: str
    user_password: str
    birthday: datetime
    phone_number: str
    time_stamp: datetime
    # todos: list["Todo"]


class UserResponse(SQLModel):
    id: int
    user_name: str
    user_email: str
    user_password: str
    birthday: datetime
    phone_number: str
    time_stamp: datetime
    # todos: list["Todo"]

class UserUpdate(SQLModel):
    user_name: str | None = None
    user_email: str | None = None
    user_password: str | None = None
    birthday: datetime | None = None
    phone_number: str | None = None
    time_stamp: datetime | None = None
    # todos: list["Todo"] | None = None

#Project Class Models

class Project(SQLModel, table=True):
    id: int = Field(default=None,primary_key=True)
    project_name: str  = Field(index=True)
    status: str = Field(default="undone")
    time_stamp: datetime = Field(sa_column_kwargs={"default": datetime.now(timezone.utc)})
    todos: list["Todo"] = Relationship(back_populates="project")


class CreateProject(SQLModel):
    project_name: str
    status: str
    time_stamp: datetime
    # todos: list["Todo"] 

    

    
class ProjectResponse(SQLModel):
    id: int
    project_name: str
    status: str
    time_stamp: datetime
    # todos: list["Todo"]

class ProjectUpdate(SQLModel):
    project_name: str | None = None
    status: str | None = None
    time_stamp: datetime | None = None
    # todos: list["Todo"] | None = None


#Todo Class Models 

class Todo(SQLModel, table=True):
    id: int|None = Field(default=None,primary_key=True)
    name: str = Field(index=True)
    body: str 
    status: str
    due_date: datetime = Field(sa_column_kwargs={"default": datetime.now()})
    time_stamp: datetime  = Field(sa_column_kwargs={"default": datetime.now()})
    project_id: int | None = Field(default=None, foreign_key='project.id')
    project: Project | None = Relationship(back_populates="todos")
    users: list[User] = Relationship(back_populates="todos",link_model=UserTodoLink)

class TodoCreate(SQLModel):
    name: str
    body: str
    status: str
    due_date: datetime 
    time_stamp: datetime
    project_id: int | None = None

class TodoResponse(SQLModel):
    id: int
    name: str
    body: str
    status: str
    due_date: datetime
    time_stamp: datetime 
    project_id: int | None = None

class TodoUpdate(SQLModel):
    name: str | None = None
    body: str | None = None
    status: str | None = None
    due_date: datetime | None = None
    time_stamp: datetime | None = None
    project_id: int | None = None
    project: Project | None = None


from sqlmodel import SQLModel, Field, create_engine, Session



class Todo(SQLModel, table=True):
    id: int|None = Field(default=None,primary_key=True)
    name: str = Field(index=True)
    body: str 
    status: str

class TodoCreate(SQLModel):
    name: str
    body: str
    status: str


class TodoResponse(SQLModel):
    id: int
    name: str
    body: str
    status: str

class TodoUpdate(SQLModel):
    name: str | None = None
    body: str | None = None
    status: str | None = None

     
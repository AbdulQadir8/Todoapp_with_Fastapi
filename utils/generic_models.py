from sqlmodel import SQLModel, Field



class UserTodoLink(SQLModel, table=True):
    user_id: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
    todo_id: int | None = Field(default=None, foreign_key="todo.id", primary_key=True)
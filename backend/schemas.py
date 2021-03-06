from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str


class TaskUpdate(TaskBase):
    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

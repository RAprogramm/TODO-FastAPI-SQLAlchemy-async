from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .database import get_session
from .schemas import Task, TaskUpdate

router = APIRouter()


@router.get("/", response_model=list[Task], tags=["Task"])
async def get_tasks(session: AsyncSession = Depends(get_session)):
    return await crud.read_tasks(session)


@router.get("/{id}", response_model=Task, tags=["Task"])
async def get_task_by_id(id: int, session: AsyncSession = Depends(get_session)):
    return await crud.read_task_by_id(id, session)


@router.post("/", response_model=Task, tags=["Task"])
async def create_task(
    title: str,
    description: str,
    session: AsyncSession = Depends(get_session),
):
    return await crud.create_task(session, title, description)


@router.put("/{id}", response_model=TaskUpdate, tags=["Task"])
async def update_task(
    id: int,
    title: str,
    description: str,
    session: AsyncSession = Depends(get_session),
):
    return await crud.update_task_by_id(id, title, description, session)


@router.delete("/", tags=["Task"])
async def remove_task(id: int, session: AsyncSession = Depends(get_session)):
    return await crud.delete_task_by_id(id, session)

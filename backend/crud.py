from sqlalchemy import delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import Task


async def create_task(session: AsyncSession, title: str, description: str):
    new_task = Task(title=title, description=description)
    session.add(new_task)
    await session.commit()


async def read_tasks(session: AsyncSession) -> list[Task]:
    result = await session.execute(select(Task).order_by(Task.id))
    return result.scalars().all()


async def read_task_by_id(id: int, session: AsyncSession):
    result = await session.execute(select(Task).where(Task.id == id).order_by(Task.id))
    return result.scalar()


async def update_task_by_id(
    id: int, title: str, description: str, session: AsyncSession
):
    task_db = update(Task).where(Task.id == id)
    if title:
        task_db = task_db.values(title=title)
    if description:
        task_db = task_db.values(description=description)
    task_db.execution_options(synchronize_session="fetch")
    await session.execute(task_db)
    await session.commit()


async def delete_task_by_id(id: int, session: AsyncSession):
    await session.execute(delete(Task).where(Task.id == id))
    await session.commit()

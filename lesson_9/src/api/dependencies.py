from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from lesson_9.src.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

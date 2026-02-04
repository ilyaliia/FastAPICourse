from fastapi import APIRouter
from sqlalchemy import select

from api.dependencies import SessionDep    # src/api
from lesson_9.src.database import engine, Base
from lesson_9.src.models.books import BookModel
from lesson_9.src.schemas.books import BookCreateSchema

router = APIRouter()


@router.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"success": True}


@router.post("/books")
async def add_book(data: BookCreateSchema, session: SessionDep):
    new_book = BookModel(
        title=data.title,
        author=data.author
    )
    session.add(new_book)
    await session.commit()
    return {"success": True}


@router.get("/books")
async def get_books(session: SessionDep):
    query = select(BookModel)
    result = await session.execute(query)
    return result.scalars().all()
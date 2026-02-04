from fastapi import APIRouter
from api.books import router as books_router  # Используем api.books

main_router = APIRouter()
main_router.include_router(books_router)
import pytest
from sqlalchemy.orm import Session
import crud, schemas

def test_create_book(db: Session):
    new_book = schemas.BookCreate(title="Test Book", author="Author", year=2024)
    created_book = crud.create_book(db=db, book=new_book)
    assert created_book.title == "Test Book"
    assert created_book.author == "Author"
    assert created_book.year == 2024

def test_get_book(db: Session):
    book = crud.get_book(db=db, book_id=1)
    assert book is not None
    assert book.title == "Test Book"

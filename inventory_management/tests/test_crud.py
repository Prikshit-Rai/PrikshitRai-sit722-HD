import pytest
from sqlalchemy.orm import Session
import crud, schemas

def test_create_item(db: Session):
    new_item = schemas.ItemCreate(name="Laptop", quantity=10)
    created_item = crud.create_item(db=db, item=new_item)
    assert created_item.name == "Laptop"
    assert created_item.quantity == 10

def test_get_item(db: Session):
    item = crud.get_item(db=db, item_id=1)
    assert item is not None
    assert item.name == "Laptop"

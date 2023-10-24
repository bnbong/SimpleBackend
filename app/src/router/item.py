# --------------------------------------------------------------------------
# Item model의 API router을 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from logging import getLogger
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.crud.item import (
    get_items,
    get_item,
    create_item,
    update_item,
    delete_item,
)
from src.db import database
from src.schemas import item as schemas


log = getLogger(__name__)
item_router = APIRouter(prefix="/item")


@item_router.get(
    "/",
    response_model=List[schemas.Item],
    summary="Read items",
    description="Read items",
)
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    log.info(f"Reading items with skip: {skip} and limit: {limit}")
    return get_items(db, skip=skip, limit=limit)


@item_router.get(
    "/{item_id}",
    response_model=schemas.Item,
    summary="Read an item",
    description="Read an item with the given id",
)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@item_router.post(
    "/",
    response_model=schemas.Item,
    summary="Create a new item",
    description="Create a new item with the given name, price, owner_id",
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return create_item(db, item)


@item_router.put(
    "/{item_id}",
    response_model=schemas.Item,
    summary="Update an item",
    description="Update an item with the given name, price",
)
def update_item(
    item_id: int, item: schemas.ItemUpdate, db: Session = Depends(database.get_db)
):
    updated_item = update_item(db, item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@item_router.delete(
    "/{item_id}",
    response_model=int,
    summary="Delete an item",
    description="Delete an item with the given id",
)
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    deleted_item_id = delete_item(db, item_id)
    if deleted_item_id is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted_item_id

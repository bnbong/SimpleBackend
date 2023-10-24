# --------------------------------------------------------------------------
# Item model의 CRUD를 담당하는 메서드를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from sqlalchemy.orm import Session

from src.db.models import Item
from src.crud._base import (
    create_object,
    get_object,
    get_objects,
    delete_object,
    update_object,
)
from src.schemas.item import ItemCreate


def create_item(db: Session, item: ItemCreate) -> Item:
    return create_object(db, Item, item)


def get_item(db: Session, item_id: int) -> Item:
    return get_object(db, Item, item_id)


def get_items(db: Session, skip: int = 0, limit: int = 100) -> Item:
    return get_objects(db, Item, skip, limit)


def update_item(db: Session, item_id: int, item: Item) -> Item:
    return update_object(db, Item, item_id, item)


def delete_item(db: Session, item_id: int) -> int:
    return delete_object(db, Item, item_id)

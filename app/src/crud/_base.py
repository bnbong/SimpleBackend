# --------------------------------------------------------------------------
# 기본 Model CRUD 메서드를 정의한 모듈입니다.
#
# @author bnbong bbbong9@gmail.com
# --------------------------------------------------------------------------
from typing import Any

from sqlalchemy.orm import Session


def get_object(db: Session, model: Any, model_id: int) -> Any:
    return db.query(model).filter(model.id == model_id).first()


def get_objects(db: Session, model: Any, skip: int = 0, limit: int = 100) -> Any:
    return db.query(model).offset(skip).limit(limit).all()


def create_object(db: Session, model: Any, obj: Any) -> Any:
    db_obj = model(**obj.model_dump())

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_object(db: Session, model: Any, model_id: int, obj: Any) -> Any:
    db_obj = get_object(db, model, model_id)
    update_data = obj.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_object(db: Session, model: Any, model_id: int) -> int:
    db.query(model).filter(model.id == model_id).delete()
    db.commit()
    return model_id

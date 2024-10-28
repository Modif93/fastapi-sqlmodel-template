from typing import Annotated, Type, Any

from fastapi import Depends
from sqlmodel import Session, SQLModel, select

from .database import get_session
from ..exception.entity import EntityNotFoundError

database_session = Annotated[Session, Depends(get_session)]


class Repository(object):
    _model: Type[SQLModel]
    _entity_name: str

    def __init__(self, _session: database_session):
        self._session = _session

    def get_all(self):
        statement = select(self._model)
        return self._session.scalars(statement).all()

    def get_by_id(self, _id):
        entity = self._session.get(self._model, _id)
        if not entity:
            raise EntityNotFoundError(self._entity_name, _id)
        return entity

    def add(self, model: Any):
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return model

    def modify(self, model: Any):
        merged_model = self._session.merge(model)
        self._session.commit()
        self._session.refresh(merged_model)
        return merged_model

    def delete_by_id(self, _id):
        entity = self._session.get(self._model, _id)
        if not entity:
            raise EntityNotFoundError(self._entity_name, _id)
        self._session.delete(entity)
        self._session.commit()

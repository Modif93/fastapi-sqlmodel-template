from abc import ABC, abstractmethod
from typing import Type, Annotated

from fastapi import Depends
from sqlmodel import SQLModel, Session

from ..core.database import get_session


class RepositoryABC(ABC):

    def __init__(self, _session: Annotated[Session, Depends(get_session)]):
        self._session = _session

    @abstractmethod
    def get_by_id(self, _session: Annotated[Session, Depends(get_session)]) -> 'Type[SQLModel]':
        raise NotImplementedError

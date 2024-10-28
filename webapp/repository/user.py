"""User Repository module."""
from sqlmodel import select
from ..core.repository import Repository
from ..model.db.user import User


class UserRepository(Repository):
    _model: User
    _entity_name: "User"

    def get_by_username(self, username):
        stmt = select(User).filter_by(username=username)
        return self._session.scalars(stmt).first()

    def get_by_uuid(self, uuid):
        stmt = select(User).filter_by(user_uuid=uuid)
        return self._session.scalars(stmt).first()

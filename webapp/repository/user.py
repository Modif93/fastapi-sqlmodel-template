"""User Repository module."""

from ..core.repository import Repository
from webapp.model.db.user import User


class UserRepository(Repository):
    _model: User
    _entity_name: "User"
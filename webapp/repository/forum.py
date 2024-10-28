from ..core.repository import Repository
from ..model.db.forum import Forum, ForumPosts


class ForumRepository(Repository):
    _model: Forum
    _entity_name: "Forum"


class ForumPostsRepository(Repository):
    _model: ForumPosts
    _entity_name: "ForumPosts"

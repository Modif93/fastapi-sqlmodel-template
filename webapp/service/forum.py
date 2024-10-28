from typing import Annotated

from fastapi import Depends

from ..repository.forum import ForumRepository

forum_repository = Annotated[ForumRepository,Depends()]
class ForumService(object):
    def __init__(self,_forum_repository: forum_repository):
        self._forum_repository = _forum_repository
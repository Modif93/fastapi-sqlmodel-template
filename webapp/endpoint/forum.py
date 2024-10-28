from typing import Annotated

from fastapi import APIRouter, Depends
from ..service.forum import ForumService
router = APIRouter()

forum_service = Annotated[ForumService,Depends()]

@router.get("/forum")
def get_all_forum(forum_service:forum_service):
    return forum_service.get_all()


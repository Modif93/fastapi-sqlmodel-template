"""Endpoints module."""
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from ..service.user import UserService
from ..exception.entity import EntityNotFoundError

router = APIRouter()

UserServiceDepend = Annotated[UserService, Depends(UserService)]


@router.get("/users")
def get_list(user_service: UserServiceDepend):
    return user_service.get_users()


@router.get("/users/{user_id}")
def get_by_id(user_id: int, user_service: UserServiceDepend):
    try:
        return user_service.get_user_by_id(user_id)
    except EntityNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/users", status_code=status.HTTP_201_CREATED)
def add(user_service: UserServiceDepend):
    return user_service.create_user()


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(user_id: int, user_service: UserServiceDepend):
    try:
        user_service.delete_user_by_id(user_id)
    except EntityNotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status")
def get_status():
    return {"status": "OK"}

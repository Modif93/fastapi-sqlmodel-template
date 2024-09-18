"""Endpoints module."""
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from ..service.user import UserService
from ..exception.entity import EntityNotFoundError
from ..exception.user import UserNotFoundException

router = APIRouter()

userService = Annotated[UserService, Depends(UserService)]


@router.get("/users")
def get_list(user_service: userService):
    return user_service.get_users()


@router.get("/users/{user_id}")
def get_by_id(user_id: int, user_service: userService):
    return user_service.get_user_by_id(user_id)


@router.post("/users", status_code=status.HTTP_201_CREATED)
def add(user_service: userService):
    return user_service.create_user()


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(user_id: int, user_service: userService):
    return user_service.delete_user_by_id(user_id)



@router.get("/status")
def get_status():
    return {"status": "OK"}

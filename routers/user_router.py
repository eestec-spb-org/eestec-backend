import os

import jwt
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer

from repositories.user_repository import UserRepository
from schemas.user_schemas import SchemaUserAdd, UserIdSchema, UserReturnSchema

import hashlib

from services.user_service import add_user
from services.auth import fastapi_users
from utils.security import create_token
from dependencies import get_request_actor


"""
Эндпоинты для работы с пользователем. Их описание в гугл доке
"""


router = APIRouter(
    prefix="/api",
    tags=["API"],
)


@router.get("/secret")
async def protected_route(
    actor: UserReturnSchema = Depends(get_request_actor)
):
    return {"secret_data": "This is top secret information!"}


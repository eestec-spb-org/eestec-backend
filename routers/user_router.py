import os

import jwt
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer

from repositories.user_repository import UserRepository
from schemas.user_schemas import SchemaUserAdd, SUserId, SUserReturn

import hashlib

from services.user_service import add_user
from utils.security import create_token


"""
Эндпоинты для работы с пользователем. Их описание в гугл доке
"""


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/api",
    tags=["API"],
)


@router.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    pass
    # TODO


@router.get("/secret")
async def protected_route(token: str = Depends(oauth2_scheme)):
    pass
    # TODO


@router.get("/me")
async def profile(token: str = Depends(oauth2_scheme)) -> SUserReturn:
    pass
    # TODO


@router.post("/register")
async def register(user_init: SchemaUserAdd = Depends()) -> SUserId:
    pass
    # TODO




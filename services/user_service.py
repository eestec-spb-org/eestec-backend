from fastapi import Depends

from repositories.user_repository import UserRepository
from schemas.user_schemas import SUserAdd, SUser
from utils.security import encrypt

"""
Сервис содержит методы для работы с репозиторией user_repository
"""

"""
Добавляет польщователя в БД, возвращает запись из БД о пользователе
"""


async def add_user(user_init: SUserAdd = Depends()) -> SUser:
    pass
    # TODO

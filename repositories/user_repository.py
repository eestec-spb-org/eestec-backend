from fastapi import HTTPException
from sqlalchemy import select
from utils.database import UserOrm, async_session
from schemas.user_schemas import SchemaUserAdd, SchemaUser

"""
Репозиторий используется для изменения данных в БД  

"""


class UserRepository:
    """
       Метод используется для возврата данных о пользователе по его email
       :param email: str
           String используется временно
           Желательно добавить: data_schemas.SEmail(username: str, mail_server: str, domain: str)
       :returns user: user_schemas.SUser
       """

    @classmethod
    async def get_user_by_email(cls, email: str) -> SchemaUser:
        pass
        # TODO

    """
    Метод используется для добавления пользователя в БД
    :param user: user_schemas.SUserAdd
    :returns id: int Временно
    :exception HTTPException 400 User already exists
    """
    @classmethod
    async def add_user(cls, user: SchemaUserAdd) -> bool:
        pass
        # TODO

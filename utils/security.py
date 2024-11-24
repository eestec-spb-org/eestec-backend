import hashlib
import os
from datetime import datetime, timedelta

import jwt

from schemas.user_schemas import SchemaUserAdd

"""
Хеширует пароль, возвращает такого же пользователя, но с защищённым паролем для записи в БД
"""
def encrypt(user_init: SchemaUserAdd) -> SchemaUserAdd:
    pass
    # TODO


"""
Создаёт JWT (JSON Web Token) по email
"""
def create_token(email: str):
    pass
    # TODO
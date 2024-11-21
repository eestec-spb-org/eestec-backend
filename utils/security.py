import hashlib
import os
from datetime import datetime, timedelta

import jwt

from schemas.user_schemas import SUserAdd

"""
Хеширует пароль, возвращает такого же пользователя, но с защищённым паролем для записи в БД
"""
def encrypt(user_init: SUserAdd) -> SUserAdd:
    pass
    # TODO


"""
Создаёт JWT (JSON Web Token) по email
"""
def create_token(email: str):
    pass
    # TODO
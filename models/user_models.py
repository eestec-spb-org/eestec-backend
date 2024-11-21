from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

"""
Тут хранятся ORM (Object-Relational Mapping) модели для перевода данных о пользователе из БД
"""


"""
Базовый класс, используется в качестве основы для новых декларативных отображений
"""


class Model(DeclarativeBase):
    pass


"""
Класс для отображения пользователя в БД
"""


class UserOrm(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()

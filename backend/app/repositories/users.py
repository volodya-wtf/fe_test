import datetime

from typing import List, Optional
from unittest import skip
from app.db.users import users
from app.models.user import User, UserIn
from .base import BaseRepository
from app.core.security import hash_password


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, offset: int = 0) -> List[User]:
        query = users.select().limit(limit).offset(offset)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn) -> User:
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)  # Удаляем автоинкрементное поле

        query = users.insert().values(**values)
        user.id = await self.database.execute(query)

        return user

    async def update(self, id: int, u: UserIn) -> User:
        user = User(
            id=id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop("id", None)  # Удаляем автоинкрементное поле
        values.pop("created_at", None)

        query = users.update().where(users.c.id == id).values(**values)
        await self.database.execute(query)

        return user

    async def get_by_email(self, email: str) -> User:
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return User.parse_obj(user)

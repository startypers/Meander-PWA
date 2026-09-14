from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

# URL для подключения к PostgreSQL (из docker-compose.yml)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://meander:password123@localhost:5432/meander_db"
)

# Создаем асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем фабрику сессий
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Функция для получения сессии БД (используется в роутерах)
async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

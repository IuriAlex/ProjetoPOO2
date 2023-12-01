from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from Fastapi.App.dependencias.config import settings

# Configuração do engine com SSL
engine = create_async_engine(
    settings.DB_URL,
    connect_args={"ssl": False}  # Configuração para desabilitar SSL
)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from Fastapi.App.dependencias.database import Session


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:  # Abre conexão
        yield session
    finally:  # Fecha conexão
        await session.close()

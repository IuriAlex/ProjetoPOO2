from App.dependencias.config import settings
from App.dependencias.database import engine
from Fastapi.App.views.models.FuncionariosModel import FuncionarioModel


async def create_tables() -> None:
    from Fastapi.App.views.models.FuncionariosModel import FuncionarioModel

    print('Criando as tabelas no banco de dados')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
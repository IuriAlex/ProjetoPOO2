from Fastapi.App.dependencias.config import settings
from Fastapi.App.dependencias.database import engine
from Fastapi.App.views.models.DepartamentosModel import DepartamentoModel
from Fastapi.App.views.models.FuncionariosModel import FuncionarioModel
from Fastapi.App.views.models.GerentesModel import GerenteModel
from Fastapi.App.views.models.ProjetosModel import ProjetoModel
from Fastapi.App.views.models.RegistroDePresencasModel import RegistroDePresencaModel
from Fastapi.App.views.models.TrabalhaEmsModel import TrabalhaEmModel



async def create_tables() -> None:
    from Fastapi.App.views.models.DepartamentosModel import DepartamentoModel
    from Fastapi.App.views.models.FuncionariosModel import FuncionarioModel
    from Fastapi.App.views.models.GerentesModel import GerenteModel
    from Fastapi.App.views.models.ProjetosModel import ProjetoModel
    from Fastapi.App.views.models.RegistroDePresencasModel import RegistroDePresencaModel
    from Fastapi.App.views.models.TrabalhaEmsModel import TrabalhaEmModel

    print('Criando as tabelas no banco de dados')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())

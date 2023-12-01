from typing import List
from fastapi import status, APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from Fastapi.App.dependencias.dep import get_session
from Fastapi.App.views.models.GerentesModel import GerenteModel
from Fastapi.App.views.schemas.GerentesSchemas import GerenteSchemas

gerente = APIRouter(tags=["Gerente"])

#Cadastrar Gerentes
@gerente.post('/CadastrarGerente', status_code=status.HTTP_201_CREATED, response_model=GerenteSchemas)
async def registra_gerente(item: GerenteSchemas, db: AsyncSession = Depends(get_session)):
    novo_gerente = GerenteModel(idGerente=item.idGerente, Funcionario_Cpf=item.Funcionario_Cpf, Funcionario_Departamento_IdDepartamento=item.Funcionario_Departamento_IdDepartamento, Departamento_IdDepartamento=item.Departamento_IdDepartamento)

    db.add(novo_gerente)
    await db.commit()

    return novo_gerente


# Listar todos os gerente
@gerente.get('/ListarGerente', response_model=List[GerenteSchemas])
async def listar_gerente(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GerenteModel)
        result = await session.execute(query)
        Get_list: List[GerenteModel] = result.scalars().unique().all()

        return Get_list


# Gerente por codigo
@gerente.get('/ListarGerente{codigo_gerente}', response_model=GerenteSchemas, status_code=status.HTTP_200_OK)
async def list_gerente(codigo_gerente: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GerenteModel).filter(GerenteModel.codigo == codigo_gerente)
        result = await session.execute(query)
        artigo: GerenteModel = result.scalars().unique().one_or_none()

        if artigo:
            return artigo
        else:
            raise HTTPException(detail='Gerente não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# Alterar Gerente
@gerente.put('/AlteracaoGerente{codigo_gerente}', response_model=GerenteSchemas, status_code=status.HTTP_202_ACCEPTED)
async def alteracao_gerente(codigo_gerente: int, item: GerenteSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GerenteModel).filter(GerenteModel.codigo == codigo_gerente)
        result = await session.execute(query)
        Get_up: GerenteModel = result.scalars().unique().one_or_none()

        if Get_up:
            Get_up.idGerente = item.idGerente
            Get_up.Funcionario_Cpf = item.Funcionario_Cpf
            Get_up.Funcionario_Departamento_IdDepartamento = item.Funcionario_Departamento_IdDepartamento
            Get_up.Departamento_IdDepartamento = item.Departamento_IdDepartamento

            await session.commit()
            return Get_up
        else:
            raise HTTPException(detail="Código gerente não encontrado.", status_code=status.HTTP_404_NOT_FOUND)

# Deletar gerente
@gerente.delete('/DeletarGerente{codigo_gerente}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_gerente(codigo_gerente: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(GerenteModel).filter(GerenteModel.codigo == codigo_gerente)
        result = await session.execute(query)
        Get_del = result.scalar_one_or_none()

        if Get_del:
            await session.delete(Get_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Código gerente não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
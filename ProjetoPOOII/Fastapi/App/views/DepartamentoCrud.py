from typing import List
from fastapi import status, APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from Fastapi.App.dependencias.dep import get_session
from Fastapi.App.views.models.DepartamentosModel import DepartamentoModel
from Fastapi.App.views.schemas.DepartamentosSchemas import DepartamentoSchemas

departamento = APIRouter(tags=["Departamento"])

#Cadastrar Departamentos
@departamento.post('/CadastrarDepartamento', status_code=status.HTTP_201_CREATED, response_model=DepartamentoSchemas)
async def registra_departamento(item: DepartamentoSchemas, db: AsyncSession = Depends(get_session)):
    novo_departamento = DepartamentoModel(IdDepartamento=item.IdDepartamento, Nome=item.Nome, Descricao=item.Descricao)

    db.add(novo_departamento)
    await db.commit()

    return novo_departamento


# Listar todos os departamento
@departamento.get('/ListarDepartamento', response_model=List[DepartamentoSchemas])
async def listar_departamento(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DepartamentoModel)
        result = await session.execute(query)
        Dep_list: List[DepartamentoModel] = result.scalars().all()

        return Dep_list


# Departamento por codigo
@departamento.get('/ListarDepartamento/{codigo_departamento}', response_model=DepartamentoSchemas, status_code=status.HTTP_200_OK)
async def list_departamento(codigo_departamento: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DepartamentoModel).filter(DepartamentoModel.codigo == codigo_departamento)
        result = await session.execute(query)
        artigo: DepartamentoModel = result.scalars().unique().one_or_none()

        if artigo:
            return artigo
        else:
            raise HTTPException(detail='Departamento não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# Alterar Departamento
@departamento.put('/AlteracaoDepartamento/{codigo_departamento}', response_model=DepartamentoSchemas, status_code=status.HTTP_202_ACCEPTED)
async def alteracao_departamento(codigo_departamento: int, item: DepartamentoSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DepartamentoModel).filter(DepartamentoModel.codigo == codigo_departamento)
        result = await session.execute(query)
        Dep_up: DepartamentoModel = result.scalars().unique().one_or_none()

        if Dep_up:
            Dep_up.IdDepartamento = item.IdDepartamento
            Dep_up.Nome = item.Nome
            Dep_up.Descricao = item.Descricao

            await session.commit()
            return Dep_up
        else:
            raise HTTPException(detail="Código departamento não encontrado.", status_code=status.HTTP_404_NOT_FOUND)

# Deletar departamento
@departamento.delete('/DeletarDepartamento/{codigo_departamento}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_departamento(codigo_departamento: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(DepartamentoModel).filter(DepartamentoModel.codigo == codigo_departamento)
        result = await session.execute(query)
        Dep_del = result.scalar_one_or_none()

        if Dep_del:
            await session.delete(Dep_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Código departamento não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
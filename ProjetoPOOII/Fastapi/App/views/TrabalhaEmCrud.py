from typing import List
from fastapi import status, APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from Fastapi.App.dependencias.dep import get_session
from Fastapi.App.views.models.TrabalhaEmsModel import TrabalhaEmModel
from Fastapi.App.views.schemas.TrabalhaEmsSchemas import TrabalhaEmSchemas

trabalhaEm = APIRouter(tags=["TrabalhaEm"])

#Cadastrar TrabalhaEms
@trabalhaEm.post('/CadastrarTrabalhaEm', status_code=status.HTTP_201_CREATED, response_model=TrabalhaEmSchemas)
async def registra_trabalhaEm(item: TrabalhaEmSchemas, db: AsyncSession = Depends(get_session)):
    novo_trabalhaEm = TrabalhaEmModel(idTrabalhaEm=item.idTrabalhaEm, Projeto_IDProjeto=item.Projeto_IDProjeto, Funcionario_Cpf=item.Funcionario_Cpf, Funcionario_Departamento_IdDepartamento=item.Funcionario_Departamento_IdDepartamento)

    db.add(novo_trabalhaEm)
    await db.commit()

    return novo_trabalhaEm


# Listar todos os trabalhaEm
@trabalhaEm.get('/ListarTrabalhaEm', response_model=List[TrabalhaEmSchemas])
async def listar_trabalhaEm(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TrabalhaEmModel)
        result = await session.execute(query)
        Tra_list: List[TrabalhaEmModel] = result.scalars().unique().all()

        return Tra_list


# TrabalhaEm por codigo
@trabalhaEm.get('/ListarTrabalhaEm{codigo_trabalhaEm}', response_model=TrabalhaEmSchemas, status_code=status.HTTP_200_OK)
async def list_trabalhaEm(codigo_trabalhaEm: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TrabalhaEmModel).filter(TrabalhaEmModel.codigo == codigo_trabalhaEm)
        result = await session.execute(query)
        artigo: TrabalhaEmModel = result.scalars().unique().one_or_none()

        if artigo:
            return artigo
        else:
            raise HTTPException(detail='TrabalhaEm não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# Alterar TrabalhaEm
@trabalhaEm.put('/AlteracaoTrabalhaEm{codigo_trabalhaEm}', response_model=TrabalhaEmSchemas, status_code=status.HTTP_202_ACCEPTED)
async def alteracao_trabalhaEm(codigo_trabalhaEm: int, item: TrabalhaEmSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TrabalhaEmModel).filter(TrabalhaEmModel.codigo == codigo_trabalhaEm)
        result = await session.execute(query)
        Tra_up: TrabalhaEmModel = result.scalars().unique().one_or_none()

        if Tra_up:
            Tra_up.idTrabalhaEm = item.idTrabalhaEm
            Tra_up.Projeto_IDProjeto = item.Projeto_IDProjeto
            Tra_up.Funcionario_Cpf = item.Funcionario_Cpf
            Tra_up.Funcionario_Departamento_IdDepartamento = item.Funcionario_Departamento_IdDepartamento

            await session.commit()
            return Tra_up
        else:
            raise HTTPException(detail="Código trabalhaEm não encontrado.", status_code=status.HTTP_404_NOT_FOUND)

# Deletar trabalhaEm
@trabalhaEm.delete('/DeletarTrabalhaEm{codigo_trabalhaEm}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_trabalhaEm(codigo_trabalhaEm: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TrabalhaEmModel).filter(TrabalhaEmModel.codigo == codigo_trabalhaEm)
        result = await session.execute(query)
        Tra_del = result.scalar_one_or_none()

        if Tra_del:
            await session.delete(Tra_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Código trabalhaEm não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
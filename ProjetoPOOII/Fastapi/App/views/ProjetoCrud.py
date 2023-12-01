from typing import List
from fastapi import status, APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from Fastapi.App.dependencias.dep import get_session
from Fastapi.App.views.models.ProjetosModel import ProjetoModel
from Fastapi.App.views.schemas.ProjetosSchemas import ProjetoSchemas

projeto = APIRouter(tags=["Projeto"])

#Cadastrar Projetos
@projeto.post('/CadastrarProjeto', status_code=status.HTTP_201_CREATED, response_model=ProjetoSchemas)
async def registra_projeto(item: ProjetoSchemas, db: AsyncSession = Depends(get_session)):
    novo_projeto = ProjetoModel(IDProjeto=item.IDProjeto, Nome=item.Nome, Departamento_IdDepartamento=item.Departamento_IdDepartamento)

    db.add(novo_projeto)
    await db.commit()

    return novo_projeto


# Listar todos os projeto
@projeto.get('/ListarProjeto', response_model=List[ProjetoSchemas])
async def listar_projeto(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProjetoModel)
        result = await session.execute(query)
        Pro_list: List[ProjetoModel] = result.scalars().unique().all()

        return Pro_list


# Projeto por codigo
@projeto.get('/ListarProjeto{codigo_projeto}', response_model=ProjetoSchemas, status_code=status.HTTP_200_OK)
async def list_projeto(codigo_projeto: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProjetoModel).filter(ProjetoModel.codigo == codigo_projeto)
        result = await session.execute(query)
        artigo: ProjetoModel = result.scalars().unique().one_or_none()

        if artigo:
            return artigo
        else:
            raise HTTPException(detail='Projeto não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# Alterar Projeto
@projeto.put('/AlteracaoProjeto{codigo_projeto}', response_model=ProjetoSchemas, status_code=status.HTTP_202_ACCEPTED)
async def alteracao_projeto(codigo_projeto: int, item: ProjetoSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProjetoModel).filter(ProjetoModel.codigo == codigo_projeto)
        result = await session.execute(query)
        Pro_up: ProjetoModel = result.scalars().unique().one_or_none()

        if Pro_up:
            Pro_up.IDProjeto = item.IDProjeto
            Pro_up.Nome = item.Nome
            Pro_up.Departamento_IdDepartamento = item.Departamento_IdDepartamento

            await session.commit()
            return Pro_up
        else:
            raise HTTPException(detail="Código projeto não encontrado.", status_code=status.HTTP_404_NOT_FOUND)

# Deletar projeto
@projeto.delete('/DeletarProjeto{codigo_projeto}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_projeto(codigo_projeto: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProjetoModel).filter(ProjetoModel.codigo == codigo_projeto)
        result = await session.execute(query)
        Pro_del = result.scalar_one_or_none()

        if Pro_del:
            await session.delete(Pro_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Código projeto não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
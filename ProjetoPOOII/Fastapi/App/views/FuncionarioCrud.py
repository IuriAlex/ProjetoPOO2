from typing import List
from fastapi import status, APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from App.dependencias.dep import get_session
from Fastapi.App.views.models.FuncionariosModel import FuncionarioModel
from Fastapi.App.views.schemas.FuncionariosSchemas import FuncionarioSchemas

funcionario = APIRouter(tags=["Funcionario"])

#Cadastrar Funcionarios
@funcionario.post('/CadastrarFuncionario', status_code=status.HTTP_201_CREATED, response_model=FuncionarioSchemas)
async def registra_funcionario(item: FuncionarioSchemas, db: AsyncSession = Depends(get_session)):
    novo_funcionario = FuncionarioModel(Cpf=item.Cpf, Nome=item.Nome, Endereco=item.Endereco, Telefone=item.Telefone, Sexo=item.Sexo, Salario=item.Salario, Departamento_IdDepartamento=item.Departamento_IdDepartamento)

    db.add(novo_funcionario)
    await db.commit()

    return novo_funcionario


# Listar todos os funcionario
@funcionario.get('/ListarFuncionario', response_model=List[FuncionarioSchemas])
async def listar_funcionario(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FuncionarioModel)
        result = await session.execute(query)
        Fun_list: List[FuncionarioModel] = result.scalars().unique().all()

        return Fun_list


# Funcionario por codigo
@funcionario.get('/ListarFuncionario{codigo_funcionario}', response_model=FuncionarioSchemas, status_code=status.HTTP_200_OK)
async def list_funcionario(codigo_funcionario: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FuncionarioModel).filter(FuncionarioModel.codigo == codigo_funcionario)
        result = await session.execute(query)
        artigo: FuncionarioModel = result.scalars().unique().one_or_none()

        if artigo:
            return artigo
        else:
            raise HTTPException(detail='Funcionario não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# Alterar Funcionario
@funcionario.put('/AlteracaoFuncionario{codigo_funcionario}', response_model=FuncionarioSchemas, status_code=status.HTTP_202_ACCEPTED)
async def alteracao_funcionario(codigo_funcionario: int, item: FuncionarioSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FuncionarioModel).filter(FuncionarioModel.codigo == codigo_funcionario)
        result = await session.execute(query)
        Fun_up: FuncionarioModel = result.scalars().unique().one_or_none()

        if Fun_up:
            Fun_up.Cpf = item.Cpf
            Fun_up.Nome = item.Nome
            Fun_up.Endereco = item.Endereco
            Fun_up.Telefone = item.Telefone
            Fun_up.Sexo = item.Sexo
            Fun_up.Salario = item.Salario
            Fun_up.Departamento_IdDepartamento = item.Departamento_IdDepartamento

            await session.commit()
            return Fun_up
        else:
            raise HTTPException(detail="Código funcionario não encontrado.", status_code=status.HTTP_404_NOT_FOUND)

# Deletar funcionario
@funcionario.delete('/DeletarFuncionario{codigo_funcionario}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_funcionario(codigo_funcionario: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(FuncionarioModel).filter(FuncionarioModel.codigo == codigo_funcionario)
        result = await session.execute(query)
        Fun_del = result.scalar_one_or_none()

        if Fun_del:
            await session.delete(Fun_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Código funcionario não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
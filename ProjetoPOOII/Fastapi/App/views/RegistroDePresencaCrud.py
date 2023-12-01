from typing import List
from fastapi import status, APIRouter, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from Fastapi.App.dependencias.dep import get_session
from Fastapi.App.views.models.RegistroDePresencasModel import RegistroDePresencaModel
from Fastapi.App.views.schemas.RegistroDePresencasSchemas import RegistroDePresencaSchemas

registroDePresenca = APIRouter(tags=["RegistroDePresenca"])

#Cadastrar RegistroDePresencas
@registroDePresenca.post('/CadastrarRegistroDePresenca', status_code=status.HTTP_201_CREATED, response_model=RegistroDePresencaSchemas)
async def registra_registroDePresenca(item: RegistroDePresencaSchemas, db: AsyncSession = Depends(get_session)):
    novo_registroDePresenca = RegistroDePresencaModel(idRegistroDePresenca=item.idRegistroDePresenca, Funcionario_Cpf=item.Funcionario_Cpf, Funcionario_Departamento_IdDepartamento=item.Funcionario_Departamento_IdDepartamento, Data=item.Data, HorarioEntrada=item.HorarioEntrada, HorarioSaida=item.HorarioSaida)

    db.add(novo_registroDePresenca)
    await db.commit()

    return novo_registroDePresenca


# Listar todos os registroDePresenca
@registroDePresenca.get('/ListarRegistroDePresenca', response_model=List[RegistroDePresencaSchemas])
async def listar_registroDePresenca(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RegistroDePresencaModel)
        result = await session.execute(query)
        Reg_list: List[RegistroDePresencaModel] = result.scalars().unique().all()

        return Reg_list


# RegistroDePresenca por codigo
@registroDePresenca.get('/ListarRegistroDePresenca{codigo_registroDePresenca}', response_model=RegistroDePresencaSchemas, status_code=status.HTTP_200_OK)
async def list_registroDePresenca(codigo_registroDePresenca: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RegistroDePresencaModel).filter(RegistroDePresencaModel.codigo == codigo_registroDePresenca)
        result = await session.execute(query)
        artigo: RegistroDePresencaModel = result.scalars().unique().one_or_none()

        if artigo:
            return artigo
        else:
            raise HTTPException(detail='RegistroDePresenca não encontrado',
                                status_code=status.HTTP_404_NOT_FOUND)


# Alterar RegistroDePresenca
@registroDePresenca.put('/AlteracaoRegistroDePresenca{codigo_registroDePresenca}', response_model=RegistroDePresencaSchemas, status_code=status.HTTP_202_ACCEPTED)
async def alteracao_registroDePresenca(codigo_registroDePresenca: int, item: RegistroDePresencaSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RegistroDePresencaModel).filter(RegistroDePresencaModel.codigo == codigo_registroDePresenca)
        result = await session.execute(query)
        Reg_up: RegistroDePresencaModel = result.scalars().unique().one_or_none()

        if Reg_up:
            Reg_up.idRegistroDePresenca = item.idRegistroDePresenca
            Reg_up.Funcionario_Cpf = item.Funcionario_Cpf
            Reg_up.Funcionario_Departamento_IdDepartamento = item.Funcionario_Departamento_IdDepartamento
            Reg_up.Data = item.Data
            Reg_up.HorarioEntrada = item.HorarioEntrada
            Reg_up.HorarioSaida = item.HorarioSaida

            await session.commit()
            return Reg_up
        else:
            raise HTTPException(detail="Código registroDePresenca não encontrado.", status_code=status.HTTP_404_NOT_FOUND)

# Deletar registroDePresenca
@registroDePresenca.delete('/DeletarRegistroDePresenca{codigo_registroDePresenca}', status_code=status.HTTP_204_NO_CONTENT)
async def deletar_registroDePresenca(codigo_registroDePresenca: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(RegistroDePresencaModel).filter(RegistroDePresencaModel.codigo == codigo_registroDePresenca)
        result = await session.execute(query)
        Reg_del = result.scalar_one_or_none()

        if Reg_del:
            await session.delete(Reg_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Código registroDePresenca não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
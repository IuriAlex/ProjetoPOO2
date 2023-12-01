from typing import Optional

from pydantic import BaseModel


class TrabalhaEmSchemas(BaseModel):
    idTrabalhaEm: int
    Projeto_IDProjeto: int
    Funcionario_Cpf: int
    Funcionario_Departamento_IdDepartamento: int

    class Config:
        orm_mode = True
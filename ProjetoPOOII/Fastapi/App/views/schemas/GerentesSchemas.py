from typing import Optional

from pydantic import BaseModel


class GerenteSchemas(BaseModel):
    idGerente: int
    Funcionario_Cpf: int
    Funcionario_Departamento_IdDepartamento: int
    Departamento_IdDepartamento: int

    class Config:
        orm_mode = True
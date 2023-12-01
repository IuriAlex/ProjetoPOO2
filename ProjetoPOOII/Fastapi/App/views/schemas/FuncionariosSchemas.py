from typing import Optional

from pydantic import BaseModel


class FuncionarioSchemas(BaseModel):
    Cpf: int
    Nome: str
    Endereco: str
    Telefone: int
    Sexo: str
    Salario: int
    Departamento_IdDepartamento: int

    class Config:
        orm_mode = True
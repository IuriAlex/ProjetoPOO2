from typing import Optional

from pydantic import BaseModel


class RegistroDePresencaSchemas(BaseModel):
    idRegistroDePresenca: int
    Funcionario_Cpf: int
    Funcionario_Departamento_IdDepartamento: int
    Data: str
    HorarioEntrada: str
    HorarioSaida: str

    class Config:
        orm_mode = True
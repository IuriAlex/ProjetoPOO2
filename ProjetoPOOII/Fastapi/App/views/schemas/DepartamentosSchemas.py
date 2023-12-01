from typing import Optional

from pydantic import BaseModel


class DepartamentoSchemas(BaseModel):
    IdDepartamento: int
    Nome: str
    Descricao: str

    class Config:
        orm_mode = True
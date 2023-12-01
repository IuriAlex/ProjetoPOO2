from typing import Optional

from pydantic import BaseModel


class ProjetoSchemas(BaseModel):
    IDProjeto: int
    Nome: str
    Departamento_IdDepartamento: int

    class Config:
        orm_mode = True
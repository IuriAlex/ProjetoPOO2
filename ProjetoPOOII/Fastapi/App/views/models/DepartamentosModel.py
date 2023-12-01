from Fastapi.App.dependencias.config import Settings
from sqlalchemy import Integer, String, Column, ForeignKey


class DepartamentoModel(Settings.DBBaseModel):
    __tablename__ = 'Departamento'

    IdDepartamento = Column(Integer, primary_key=True)
    Nome = Column(String(256))
    Descricao = Column(String(256))
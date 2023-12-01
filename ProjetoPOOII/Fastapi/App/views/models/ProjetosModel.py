from Fastapi.App.dependencias.config import Settings
from sqlalchemy import Integer, String, Column, ForeignKey


class ProjetoModel(Settings.DBBaseModel):
    __tablename__ = 'Projeto'

    IDProjeto = Column(Integer, primary_key=True)
    Nome = Column(String(256))
    Departamento_IdDepartamento = Column(Integer, ForeignKey("Departamento.IdDepartamento"))
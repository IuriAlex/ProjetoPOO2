from Fastapi.App.dependencias.config import Settings
from sqlalchemy import Integer, String, Column, ForeignKey


class TrabalhaEmModel(Settings.DBBaseModel):
    __tablename__ = 'TrabalhaEm'
    idTrabalhaEm = Column(Integer, primary_key=True)
    Projeto_IDProjeto = Column(Integer, ForeignKey("Projeto.IDProjeto"))
    Funcionario_Cpf = Column(Integer, ForeignKey("Funcionario.Cpf"))
    Funcionario_Departamento_IdDepartamento = Column(Integer, ForeignKey("Funcionario.Departamento_IdDepartamento"))
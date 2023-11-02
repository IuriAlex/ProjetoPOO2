from App.dependencias.config import Settings
from sqlalchemy import Integer, String, Column, ForeignKey


class FuncionarioModel(Settings.DBBaseModel):
    __tablename__ = 'Funcionario'

    Cpf = Column(Integer, primary_key=True)
    Nome = Column(String(256))
    Endereco = Column(String(256))
    Telefone = Column(Integer)
    Sexo = Column(String(10))
    Salario = Column(Integer)
    Departamento_IdDepartamento = Column(Integer, ForeignKey("Departamento.IdDepartamento"))
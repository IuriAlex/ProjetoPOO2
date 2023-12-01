from Fastapi.App.dependencias.config import Settings
from sqlalchemy import Integer, String, Column, ForeignKey


class RegistroDePresencaModel(Settings.DBBaseModel):
    __tablename__ = 'RegistroDePresenca'

    idRegistroDePresenca = Column(Integer, primary_key=True)
    Funcionario_Cpf = Column(Integer, ForeignKey("Funcionario.Cpf"))
    Funcionario_Departamento_IdDepartamento = Column(Integer, ForeignKey("Funcionario.Departamento_IdDepartamento"))
    Data = Column(String(45))
    HorarioEntrada = Column(String(45))
    HorarioSaida = Column(String(45))
from sqlalchemy import Column, Integer, String #Importa os tipos de dados para criar as colunas da tabela "veiculos" no banco de dados.
from app.db.database import Base #Importa a classe Base do arquivo database.py para criar a tabela "veiculos" no banco de dados.

#Classe para criar veículos no banco de dados, cada atributo é uma coluna na tabela "veiculos".
class Veiculo(Base):
    __tablename__ = "veiculos"
    
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True, nullable=False)
    modelo = Column(String, index=True, nullable=False)
    ano = Column(Integer, nullable=False)
    cor = Column(String, nullable=False)
    placa = Column(String, unique=True, index=True, nullable=False)
   
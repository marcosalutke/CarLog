from sqlalchemy.orm import Session 
from app.models.veiculo import Veiculo
from app.schemas import veiculo as schemas

# Busca veículo por placa. 
def get_veiculo_by_placa(db: Session, placa: str):
    return db.query(Veiculo).filter(Veiculo.placa == placa).first()

#Lista todos os veículos, com filtro de skip e limit. 
def get_veiculos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Veiculo).offset(skip).limit(limit).all()

#Salva um novo veículo no banco de dados.
def create_veiculo(db: Session, veiculo: schemas.VeiculoCreate): 
     # Transforma o schema de entrada em um modelo de banco de dados.
    db_veiculo = Veiculo(
        marca=veiculo.marca,
        modelo=veiculo.modelo,
        ano=veiculo.ano,
        placa=veiculo.placa,
        cor=veiculo.cor
    )

    db.add(db_veiculo) #Adiciona ao banco de dados.
    db.commit() #Salva as mudanças.    
    db.refresh(db_veiculo) #Atualiza o objeto com dados no banco de dados.
    return db_veiculo #Retorna o veículo recém-criado.

    
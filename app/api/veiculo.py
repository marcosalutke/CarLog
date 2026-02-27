from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas import veiculo as schemas 
from app.crud import veiculo as crud

#Rota para veículos
router = APIRouter(prefix="/veiculos", tags=["veiculos"])

#Função que recebe os dados do usuário e salva no banco de dados. (POST)
@router.post("/", response_model=schemas.VeiculoResponse)
def criar_veiculo(veiculo: schemas.VeiculoCreate, db: Session = Depends(get_db)):
    try:
        print("\n>>> [RADAR 1] O pedido chegou no balcão do FastAPI!")
        novo_veiculo = crud.create_veiculo(db, veiculo)
        print(f"\n>>> [RADAR 2] Veículo criado com sucesso: {novo_veiculo}")
        return novo_veiculo
    except Exception as e:
        # Captura qualquer erro inesperado e retorna uma mensagem de erro genérica.
        print(f"\n>>> [ERRO FATAL CAPTURADO]: {e}\n")
        raise HTTPException(status_code=500, detail=f"Erro interno detectado: {e}")

#Função para listar (GET)
@router.get("/", response_model=List[schemas.VeiculoResponse])
def listar_veiculos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    veiculos = crud.get_veiculos(db, skip=skip, limit=limit)
    return veiculos
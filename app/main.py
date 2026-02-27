from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.veiculo import Veiculo
from app.api import veiculo as rotas_veiculo

#Cria tabelas no banco de dados. Se não existirem, ele cria. Se já existirem, ele ignora. 
Base.metadata.create_all(bind=engine)   

app = FastAPI(title="CarLog API", version="0.1.0")

app.include_router(rotas_veiculo.router)

@app.get("/")
def read_root():
    return {"mensagem": "CarLog API operante e pronta para acelerar."}
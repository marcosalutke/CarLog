import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Pega URL de conexão do banco de dados do arquivo .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Trava de Segurança para garantir que a variável de ambiente foi carregada corretamente.
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("ERRO FATAL: A variável DATABASE_URL não foi encontrada no arquivo .env!")

# Correção para compatibilidade com SQLAlchemy (Supabase usa postgres:// mas o SQLAlchemy exige postgresql://)
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# O Engine é o motor que gerencia a comunição com o banco de dados(Supabase)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# A Sessão é o que usamos para fazer consultas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#A Base é a classe mãe para criar as tabelas 
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from pydantic import BaseModel, Field
from typing import Optional

# A Base: Tudo que um veículo precisa
class VeiculoBase(BaseModel):
    marca: str = Field(..., description = "Marca do fabricante", examples = ["Chevrolet"])
    modelo: str = Field(..., description = "Modelo do veículo", examples = ["Onix"])
    ano: int = Field(..., description = "Ano de fabricação do veículo", examples = [2018])
    cor: Optional[str] = Field(None, description = "Cor do veículo", examples = ["Branco"])
    placa: str = Field(..., description = "Placa do veículo", examples = ["ABC-1234", "ABC1D23"])

# Contrato de entrada para criar um veículo. Tudo o que o usuário fornece. (POST da API)
class VeiculoCreate(VeiculoBase):
    pass  #Herda tudo da Base, sem adicionar nada novo. 

# Contrato de saída para retornar um veículo. Tudo o que o usuário vê. (Devolução da API no GET)
class VeiculoResponse(VeiculoBase):
    id: int #Quando o veículo é criado, ele cria um ID no banco.  

    class Config:
        from_attributes = True #Traduz de SQLAlchemy para Pydantic (JSON) automaticamente.


   
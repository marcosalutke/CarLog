🚗 CarLog API
Monitoramento Veicular Inteligente: Integrando Telemetria e Engenharia de Software para Manutenção Preditiva.

📌 Visão Geral
O CarLog é uma solução de backend robusta que une a Engenharia Mecânica/Elétrica ao desenvolvimento de software moderno. O objetivo central é transformar a gestão veicular reativa em uma estratégia preditiva, utilizando dados reais do automóvel para antecipar falhas e otimizar custos.

Este projeto reflete minha capacidade de aplicar lógica de engenharia em sistemas de software, focando em automação de diagnósticos e integridade de dados.

🛠️ O Diferencial: Integração com Scanner OBD2
O grande diferencial técnico deste projeto é o suporte à leitura de dados via Scanners OBD2.

Análise em Tempo Real: A API foi desenhada para processar fluxos de dados vindos diretamente da ECU (unidade de controle eletrônico) do veículo.

Manutenção Preditiva Personalizada: Mesmo sem o controle total dos atuadores, o sistema utiliza o scanner para realizar uma análise diagnóstica do estado real e atual do carro (temperatura, sensores de oxigênio, carga de bateria, códigos DTC).

Inteligência de Dados: Em vez de depender de calendários fixos, os alertas de manutenção são gerados com base no comportamento e desgaste real monitorado pelo hardware, oferecendo uma visão personalizada para cada veículo.

🚀 Decisões Técnicas
Python 3.13.7 & FastAPI: Escolhi essa stack pela sua natureza assíncrona e alta performance, fundamental para lidar com a recepção de logs de sensores em tempo real sem gargalos.

PostgreSQL (Supabase): Persistência de dados com foco em integridade referencial, garantindo que o histórico de telemetria e custos financeiros esteja sempre seguro e disponível.

Tipagem Estrita (Pydantic): Uso intensivo de schemas para validar dados de hardware, evitando que inconsistências do scanner comprometam a base de dados.

✨ Funcionalidades Principais
[x] Processamento de Diagnósticos OBD2: Endpoint preparado para receber e interpretar parâmetros de sensores automotivos.

[x] Sistema de Alertas Preditivos: Geração de notificações baseadas na análise de saúde do veículo em tempo real.

[x] Gestão Financeira de Manutenções: Controle detalhado de gastos com peças, serviços e insumos.

[x] Documentação Automática: Interface Swagger (OpenAPI) integrada para testes rápidos de integração via /docs.

🏗️ Estrutura do Projeto
O projeto segue padrões de Clean Code e organização em camadas:

Plaintext
├── app/
│   ├── api/          # Endpoints e Gerenciamento de Rotas
│   ├── core/         # Configurações de ambiente e segurança
│   ├── models/       # Modelos do Banco de Dados (SQLAlchemy)
│   ├── schemas/      # Validação de dados e Tipagem (Pydantic)
│   └── services/     # Lógica de negócio e Processamento OBD2
├── main.py           # Ponto de entrada da aplicação
└── requirements.txt  # Lista de dependências

🚦 Como Executar

Clone o repositório:
git clone https://github.com/marcosalutke/CarLog.git

Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale as dependências:
Bash
pip install -r requirements.txt

Inicie o servidor localmente:
Bash
uvicorn main:app --reload

📈 A engenharia por trás do projeto
O CarLog nasceu da vontade de eliminar a incerteza na manutenção veicular. O próximo passo do projeto é a implementação de um módulo de Machine Learning leve para identificar padrões de falhas futuras com base no histórico de dados do scanner OBD2, elevando ainda mais o nível de precisão das manutenções preditivas.

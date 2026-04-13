🚗 CarLog API
API REST de Gerenciamento Veicular focada em performance, escalabilidade e organização de dados.

📌 Sobre o Projeto
O CarLog nasceu de uma necessidade real de centralizar e automatizar o histórico de manutenção e custos operacionais de veículos. Em um cenário onde o controle de gastos automotivos ainda é feito em planilhas manuais ou papel, a CarLog API oferece uma interface robusta para que proprietários e gestores tenham dados precisos na palma da mão.

Este projeto reflete minha transição da Engenharia de Hardware/Mecânica para a Engenharia de Software, aplicando lógica rigorosa de manutenção preditiva em um ambiente digital moderno.

🚀 Por que esta Stack?
A escolha das tecnologias foi baseada em critérios de mercado e eficiência técnica:

Python 3.13.7: Utilização da versão mais recente para aproveitar melhorias de performance e tipagem.

FastAPI: Escolhido pela alta performance (comparável a NodeJS e Go) e pela geração automática de documentação (Swagger), o que acelera o ciclo de desenvolvimento e integração.

PostgreSQL & Supabase: Garantia de integridade referencial para dados críticos (financeiro e mecânico). O Supabase foi utilizado como camada de persistência para facilitar o deploy e a escalabilidade.

Docker: Para garantir que o ambiente de desenvolvimento seja idêntico ao de produção, facilitando o onboarding de novos desenvolvedores e a automação de CI/CD.

🛠️ Funcionalidades Principais
[x] Gestão de Veículos: Cadastro completo com marca, modelo, ano e placa.

[x] Log de Manutenções: Registro detalhado de intervenções (óleo, freios, elétrica) com datas e custos.

[x] Controle de Abastecimento: Monitoramento de consumo médio e eficiência por combustível.

[x] Documentação Automática: Endpoint /docs integrado para testes rápidos da API.

[ ] Módulo de Alertas (Beta): Notificação automática para revisões baseada em quilometragem estimada.

🏗️ Arquitetura e Estrutura
O projeto segue padrões de Clean Code e separação de responsabilidades:

Plaintext
├── app/
│   ├── api/          # Endpoints e Rotas
│   ├── core/         # Configurações globais e segurança
│   ├── models/       # Modelos do Banco de Dados (SQLAlchemy)
│   ├── schemas/      # Validação de dados e Tipagem (Pydantic)
│   └── services/     # Lógica de negócio (Regras de manutenção)
├── docker-compose.yml
├── Dockerfile
└── main.py
🚦 Como Rodar o Projeto
Clone o repositório:

Bash
git clone https://github.com/seu-usuario/carlog-api.git
Configure as variáveis de ambiente:
Crie um arquivo .env com suas credenciais do PostgreSQL/Supabase.

Suba o container Docker:

Bash
docker-compose up -d
Acesse a documentação:
Acesse http://localhost:8000/docs para visualizar o Swagger UI.

📈 Resultado Final e Evolução
O resultado é uma API resiliente, com baixo tempo de resposta e pronta para ser consumida por aplicações Web ou Mobile.

Próximos passos:

Implementação de Testes Unitários com pytest.

Integração de Autenticação JWT.

Dashboard visual para análise de gastos mensais.

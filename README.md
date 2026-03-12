# Sistema de Controle de Estoque

Projeto desenvolvido para praticar backend com **Python** e **PostgreSQL**, focado em operações CRUD, manipulação de banco de dados e construção de consultas dinâmicas.

## Tecnologias utilizadas

- Python
- PostgreSQL
- psycopg2

## Funcionalidades

- Inserção de produtos
- Listagem de produtos
- Atualização de dados
- Exclusão de produtos
- Sistema de filtros dinâmicos por:
  - ID
  - Nome
  - Preço
  - Estoque
  - Data de criação

## Estrutura do projeto

main.py -> fluxo principal do sistema
functions.py -> lógica e queries do banco de dados
UI.py -> interface e validações de entrada


## Como executar o projeto

1. Criar banco de dados PostgreSQL
2. Criar a tabela utilizando o arquivo: database.sql
3. Configurar variáveis de ambiente
4. Executar o sistema: python main.py


## Próximos passos

- Refatorar o projeto utilizando **SQLAlchemy**
- Transformar o sistema em uma **API com FastAPI**
- Implementar novas funcionalidades de estoque:
  - Estoque máximo
  - Estoque mínimo
  - Ponto de ruptura
  - Ponto de pedido



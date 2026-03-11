# Sistema de Controle de Estoque

Projeto desenvolvido para praticar backend com Python e PostgreSQL.

## Tecnologias utilizadas

- Python
- PostgreSQL
- psycopg2

## Funcionalidades

- Inserir produtos
- Listar produtos
- Atualizar produtos
- Deletar produtos
- Filtros dinâmicos (ID, nome, preço, estoque e data)

## Estrutura do projeto

main.py → fluxo principal do sistema  
functions.py → lógica do banco de dados  
UI.py → interface e validações

## Como executar

1. Criar banco PostgreSQL
2. Criar tabela products
4. Configurar variáveis de ambiente
5. Executar:

table products.sql

python main.py

## Próximos passos

- Refatorar usando SQLAlchemy
- Transformar em API usando FastAPI
Adicionar novas funções como:
- Estoque Máximo
- Estoque Mínimo
- Ponto de ruptura
- Ponto de pedido

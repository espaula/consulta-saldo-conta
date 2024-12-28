# Serviço de Consulta de Saldo

Este é um serviço simples de consulta de saldo de conta. Ele expõe um endpoint RESTful que recebe um `id_conta` e retorna o saldo da conta.

# Tecnologias Utilizadas
     Python 3.x
     Flask para implementação do serviço web.
     Prometheus Flask Exporter para monitoramento de métricas.
     Pytest para testes unitários.
     Docker & Docker Compose.
     HTTP Client para comunicação com a API Mock.

## Pré-requisitos

- Python 3.x
- Docker e Docker Compose instalados.

## Instruções para Executar o Projeto

1. Clone o repositório.
2. Instale as dependências com o comando:

   ```bash
   pip install -r requirements.txt
  
   docker-compose up --build

## Acessar os Endpoints
API Principal: http://localhost:5000/saldo/<id_conta>
Mock API: http://localhost:5001/mock/saldo/<id_conta>
Métricas: http://localhost:5000/metrics

## Executar os Testes
 ```bash
      pytest

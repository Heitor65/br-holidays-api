# 📅 API de Feriados Brasileiros

Este projeto é uma API REST simples para consulta de feriados nacionais e estaduais do Brasil.  
A ideia é centralizar informações de datas comemorativas e feriados em um formato fácil de consumir por aplicações web, mobile ou scripts.

> ⚠️ Projeto ainda em desenvolvimento.

---

## 🚀 Funcionalidades

- Listar feriados nacionais
- (Em desenvolvimento) Suporte a feriados estaduais
- Retornar nome, data e descrição de cada feriado
- Estrutura preparada para expansão de novas datas comemorativas

---

## 🧠 Objetivo do projeto

Este projeto foi criado com fins de estudo e prática de:

- Desenvolvimento de APIs REST com Python
- Estruturação de projetos backend
- Organização de dados com modelos
- Boas práticas de código
- Evolução para um serviço mais completo no futuro (banco de dados, autenticação etc.)

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- Pydantic (validação de dados)
- JSON (formato de resposta)

---

## 📡 Endpoints

### GET `/feriados/nacionais`

Retorna todos os feriados nacionais cadastrados.

#### Exemplo de resposta

```json
[
  {
    "name": "Confraternização Universal",
    "date": {
      "day": 1,
      "month": 1
    },
    "description": "Celebra o início do ano novo."
  }
]

# 📅 API de Feriados Brasileiros

Este projeto é uma API REST simples para consulta de feriados nacionais e estaduais do Brasil.  
A ideia é centralizar informações de datas comemorativas e feriados em um formato fácil de consumir por aplicações web, mobile ou scripts.

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
    "date": {
      "day": 23,
      "month": 4
    },
    "description": "Homenageia o Santo Guerreiro, símbolo de resistência e fé, celebrado pelo sincretismo com Ogum",
    "name": "Dia de São Jorge"
  }
]

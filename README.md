# 📅 API de Feriados Brasileiros

API REST que retorna exclusivamente feriados com respaldo jurídico nacional e estadual para setor privado e público, diferenciando feriados fixos, móveis baseados na Páscoa e datas específicas por UF.

---

## 🚀 Funcionalidades

- Listar feriados nacionais
- Suporte a feriados estaduais
- Retornar nome, data e descrição de cada feriado
- Estrutura preparada para expansão de novas datas comemorativas

---

## 🧠 Objetivo do projeto

Este projeto foi criado com fins de estudo e prática de:

- Desenvolvimento de APIs REST com Python
- Estruturação de projetos backend

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- Pydantic

---

## 📡 Endpoints

### GET `nacionais/<id>`

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
```

### GET `estaduais/<uf>/<id>`

Retorna todos os feriados estaduais/distritais cadastrados.

``` JSON
[
  {
    "date": {
      "day": 9,
      "month": 7
    },
    "description": "Celebra a Data Magna do estado, que homenageia o início do levante armado de 1932 contra o governo de Getúlio Vargas.",
    "name": "Revolução Constitucionalista de 1932"
  }
]
```

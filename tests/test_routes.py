def test_nacional_retorna_200(client):
    response = client.get('/nacional')
    assert response.status_code == 200

def test_nacional_retorna_lista(client):
    response = client.get('/nacional')
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_nacional_estrutura_do_feriado(client):
    response = client.get('/nacional')
    feriado = response.get_json()[0]
    assert 'name' in feriado
    assert 'date' in feriado
    assert 'description' in feriado
    assert 'day' in feriado['date']
    assert 'month' in feriado['date']

def test_estadual_uf_valida(client):
    response = client.get('/estaduais/AL')
    assert response.status_code == 200

def test_estadual_uf_invalida(client):
    response = client.get('/estaduais/XX')
    assert response.status_code == 404

def test_nacional_com_ano_retorna_sexta_santa(client):
    response = client.get('/nacional?ano=2025')
    data = response.get_json()
    nomes = [f['name'] for f in data]
    assert 'Sexta-feira Santa' in nomes
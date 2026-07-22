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
    assert 'id' in feriado
    assert 'name' in feriado
    assert 'date' in feriado
    assert 'description' in feriado
    assert 'day' in feriado['date']
    assert 'month' in feriado['date']

def test_nacional_id_fixado(client):
    response = client.get('/nacional')
    data = response.get_json()
    natal = next(item for item in data if item['name'] == 'Natal')
    assert natal['id'] == 9

def test_busca_feriado_nacional_por_id(client):
    response = client.get('/nacionais/9')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 9
    assert data['name'] == 'Natal'

def test_movel_id_fixado(client):
    response = client.get('/nacional?ano=2025')
    data = response.get_json()
    sexta_santa = next(item for item in data if item['name'] == 'Sexta-feira Santa')
    assert sexta_santa['id'] == 10

def test_estadual_uf_valida(client):
    response = client.get('/estaduais/AL')
    assert response.status_code == 200

def test_estadual_uf_invalida(client):
    response = client.get('/estaduais/XX')
    assert response.status_code == 404

def test_estadual_id_fixado(client):
    response = client.get('/estaduais/DF')
    feriado = response.get_json()[0]
    assert feriado['id'] == 161

def test_busca_feriado_estadual_por_id(client):
    response = client.get('/estaduais/DF/161')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 161
    assert data['name'] == 'Dia do Evangélico'

def test_busca_feriado_por_id_inexistente(client):
    response = client.get('/nacionais/999')
    assert response.status_code == 404

def test_nacional_com_ano_retorna_sexta_santa(client):
    response = client.get('/nacional?ano=2025')
    data = response.get_json()
    nomes = [f['name'] for f in data]
    assert 'Sexta-feira Santa' in nomes
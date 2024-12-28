import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_consultar_saldo(client, mocker):
    mock_response = {"id_conta": 1, "saldo": 1500.75}
    mocker.patch('app.main.consultar_mock_saldo', return_value=(mock_response, 200))
    
    response = client.get('/saldo/1')
    assert response.status_code == 200
    assert response.json == mock_response


def test_consultar_saldo_nao_encontrado(client, mocker):
    mocker.patch('app.main.consultar_mock_saldo', return_value=({"error": "Conta não encontrada"}, 404))
    
    response = client.get('/saldo/99')
    assert response.status_code == 404
    assert response.json["error"] == "Conta não encontrada"
    

#def test_consultar_mock_saldo_success(mocker):
#        mock_response = mocker.Mock()
#        mock_response.json.return_value = {"id_conta": 1, "saldo": 1500.75}
#        mock_response.status_code = 200
#        mock_response.raise_for_status.return_value = None
#        mocker.patch('requests.get', return_value=mock_response)
#
#        data, status_code = consultar_mock_saldo(1)
#        assert status_code == 200
#        assert data == {"id_conta": 1, "saldo": 1500.75}
#
#
#def test_consultar_mock_saldo_not_found(mocker):
#        mock_response = mocker.Mock()
#        mock_response.json.return_value = {"error": "Conta não encontrada"}
#        mock_response.status_code = 404
#        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
#        mocker.patch('requests.get', return_value=mock_response)
#
#        data, status_code = consultar_mock_saldo(99)
#        assert status_code == 503
#        assert data == {"error": "Erro ao consultar API externa"}
#
#
#def test_consultar_mock_saldo_request_exception(mocker):
#        mocker.patch('requests.get', side_effect=requests.exceptions.RequestException("Timeout"))
#
#        data, status_code = consultar_mock_saldo(1)
#        assert status_code == 503
#        assert data == {"error": "Erro ao consultar API externa"}
#
#
import requests
import logging
from prometheus_client import Counter, Histogram,  generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, jsonify, Response

app = Flask(__name__)

# Configuração de logs
logging.basicConfig(level=logging.INFO)

# Métricas
REQUEST_COUNT = Counter('saldo_requests_total', 'Total de requisições para /saldo')
REQUEST_LATENCY = Histogram('saldo_request_latency_seconds', 'Latência das requisições')

# Função para consultar o mock
def consultar_mock_saldo(id_conta):
    try:
        response = requests.get(f"http://mock_api:5001/mock/saldo/{id_conta}", timeout=5)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Erro ao consultar Mock API: {e}")
        return {"error": "Erro ao consultar API externa"}, 503


@app.route('/saldo/<int:id_conta>', methods=['GET'])
def consultar_saldo(id_conta):
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        data, status_code = consultar_mock_saldo(id_conta)
        return jsonify(data), status_code


@app.route('/metrics', methods=['GET'])
def metrics():
    metrics_data = generate_latest()
    return Response(metrics_data, content_type=CONTENT_TYPE_LATEST), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

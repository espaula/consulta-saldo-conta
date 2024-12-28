from flask import Flask, jsonify, request

mock_app = Flask(__name__)

# Dados simulados
mock_data = {
    1: {"saldo": 1500.75},
    2: {"saldo": 300.00},
    3: {"saldo": 0.00}
}


@mock_app.route('/mock/saldo/<int:id_conta>', methods=['GET'])
def get_mock_saldo(id_conta):
    if id_conta in mock_data:
        return jsonify({"id_conta": id_conta, "saldo": mock_data[id_conta]["saldo"]}), 200
    return jsonify({"error": "Conta não encontrada"}), 404

if __name__ == "__main__":
    mock_app.run(host="0.0.0.0", port=5001)

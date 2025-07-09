from flask import Blueprint, jsonify, request

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    payload = request.json
    print(payload)
    return jsonify({
        "status": "OK",
        "payload": payload
    }),200

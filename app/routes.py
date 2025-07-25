from flask import Blueprint, jsonify, request
from app.utils.auth import require_api_key

bp = Blueprint('main', __name__)

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@bp.route('/test-upload', methods=['POST'])
@require_api_key
def test_upload():
    data = request.json
    return jsonify({"message": "Upload received", "data": data})

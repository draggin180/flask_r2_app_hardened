from flask import Blueprint, jsonify, request
from app.utils.auth import require_api_key

bp = Blueprint('main', __name__)

# Health check route
@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})


# GET /jobs – return mock job list
@bp.route('/jobs', methods=['GET'])
@require_api_key
def get_jobs():
    mock_jobs = [
        {
            "id": 1,
            "job_number": "JOB-001",
            "title": "Fix leaky faucet",
            "customer": "John Doe",
            "scheduled_date": "2025-07-26",
            "status": "Scheduled"
        },
        {
            "id": 2,
            "job_number": "JOB-002",
            "title": "Replace HVAC filter",
            "customer": "Jane Smith",
            "scheduled_date": "2025-07-27",
            "status": "Pending"
        }
    ]
    return jsonify({"jobs": mock_jobs})


# POST /jobs – add a new job (mock)
@bp.route('/jobs', methods=['POST'])
@require_api_key
def create_job():
    data = request.json
    return jsonify({"message": "Job created (mock)", "data": data}), 201

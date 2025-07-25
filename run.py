from flask import Flask
from app.routes import bp as main_routes
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.config['SECRET_API_KEY'] = os.getenv("SECRET_API_KEY")
allowed_origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

# Enable CORS
CORS(app, origins=allowed_origins)

# Setup rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[os.getenv("RATE_LIMIT", "10/minute")]
)

# Register routes
app.register_blueprint(main_routes)

# Start app
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logger.info(f"Starting app on http://localhost:{port}")
    app.run(debug=False, host='0.0.0.0', port=port)

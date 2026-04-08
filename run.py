from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.models import db
from app.routes.auth import auth_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
JWTManager(app)
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

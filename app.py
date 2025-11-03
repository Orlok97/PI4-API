from flask import Flask, jsonify
from routes import Router
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
config = Config(app)
jwt=JWTManager(app)
router = Router(app)

db.init_app(app)
with app.app_context():
   db.create_all()

@app.route('/')
def index():
    return jsonify({
       'name':'projeto integrador 4',
       'version':'0.1.0',
       'description':'API para alerta de enchentes'
    })

if __name__ == '__main__':
  app.run(debug=True)
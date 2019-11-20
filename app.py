from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from application.api import api_blueprint
from flask_cors import CORS

#instace app
app = Flask(__name__)

#load config of app
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#load sql to app
db = SQLAlchemy(app)

#load
app.register_blueprint(api_blueprint)

#cors
CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

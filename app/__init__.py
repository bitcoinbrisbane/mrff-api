from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from .db import db

# Controllers
from .opportunity.routes import opportunity
# add more here that map to the tables

load_dotenv()
CONN_STRING = os.getenv('CONN_STRING')

print('app.__init__ connstring: ' + CONN_STRING)

# no need to do migrations just yet
# migrate = Migrate(compare_type=True)


def init_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = CONN_STRING
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # migrate.init_app(app, db)

    # Register route blueprints
    app.register_blueprint(opportunity, url_prefix="/opportunity")

    # Register base route
    @app.route("/")
    def base():
        return "Hello"

    return app


app = init_app()

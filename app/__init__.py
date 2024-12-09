from flask import Flask
from .database import db
from .routes import routes  # Import your Blueprint

def create_app():
    # Initialize the Flask app
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register the Blueprint
    app.register_blueprint(routes)

    return app

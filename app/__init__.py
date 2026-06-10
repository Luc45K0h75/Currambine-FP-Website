from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address) # Initialize limiter with key function

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    # Initialise extensions
    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)  # Initialize limiter with the app for DDOS protection

    # Import models so Flask-Migrate can detect them
    from app import models

    # Register main routes
    from app import routes
    app.register_blueprint(routes.main)

    # Register team blueprint
    from app.blueprints.team import team as team_bp
    app.register_blueprint(team_bp)

    # Register fellows blueprint
    from app.blueprints.fellows import fellows as fellows_bp
    app.register_blueprint(fellows_bp)

    return app
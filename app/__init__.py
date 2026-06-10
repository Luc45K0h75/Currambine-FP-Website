from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    # Initialise extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so Flask-Migrate can detect them
    from app import models

    # Register main routes
    from app import routes
    app.register_blueprint(routes.main)

    # Register team blueprint
    from app.blueprints.team import team as team_bp
    app.register_blueprint(team_bp)

    return app
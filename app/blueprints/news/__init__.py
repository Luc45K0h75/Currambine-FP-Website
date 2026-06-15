from flask import Blueprint

news = Blueprint('news', __name__)

from app.blueprints.news import news as news_routes
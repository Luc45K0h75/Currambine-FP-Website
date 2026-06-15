from flask import render_template, request
from app.blueprints.news import news
from app.models import News

@news.route('/news')
def news_page():
    page = request.args.get('page', 1, type=int)
    posts = News.query.filter_by(published=True)\
        .order_by(News.created_at.desc())\
        .paginate(page=page, per_page=10, error_out=False)
    
    return render_template('news/news.html', posts=posts, seo={
        'title': "What's New | Currambine Family Practice",
        'description': 'Latest news and announcements from Currambine Family Practice.'
    })
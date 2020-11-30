from flask import render_template
from app import app
from .request import get_news,get_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its 
    
    '''

    news = get_news()
    return render_template('index.html', news = news)


@app.route('/source/<id>')
def article(id):

    '''
    View root page function that returns the index page and its 
    
    '''

    article= get_article(id)
    return render_template('article.html', articles= article)


    

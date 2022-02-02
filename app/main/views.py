from flask import render_template
from . import main
from ..requests import get_news,get_technews



@main.route('/')
def index():
    '''
    '''
    news=get_news()
    return render_template('index.html',articles = news)

@main.route('/tech')
def indextech():
    '''
    '''
    new=get_technews()
    return render_template('indextech.html',articles = new)

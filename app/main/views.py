# start by making all the required imports
from flask import render_template
# import the blueprint application from this very same folder
from . import main
# import request module that has all the functions for calling apis and processing the responses
from ..requests import get_categories, get_source_articles, get_trending, get_sources


# defining the homepage route
@main.route('/')
def index():
    # call the function that returns trending news
    title = 'wwn.con'
    news_title = 'Trending News'
    articles = get_trending('popularity')
    sources = get_sources()
    return render_template('index.html', articles=articles, news_title=news_title, title=title, sources=sources)


@main.route('/<cat>')
def category(cat):
    # this will be used as category title in the html
    category_title = cat.upper()
    # call get categories function which returns articles from the selected category only
    articles = get_categories(cat)
    return render_template('index.html', articles=articles, category_title=category_title)

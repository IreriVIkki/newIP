# start by making all the required imports
from flask import render_template
# import the blueprint application from this very same folder
from . import main
# import request module that has all the functions for calling apis and processing the responses
from ..requests import get_categories, get_source_articles, get_trending, get_sources, get_source_details

# define a function that formats the data recieved into lists tah caan be looped through in components giving a dopeass design in the process


def sub_arrays(array, num):
    start = 0
    articles = []
    while start < len(array):
        start2 = start
        arr2 = []
        for i in range(num):
            arr2.append(array[start2+i])
            if (start2+i) == (len(array)-1):
                break
        # print(articles)
        articles.append(arr2)
        start += num
    return articles


# defining the homepage route


@main.route('/')
def index():
    # call the function that returns trending news
    title = 'wwn.con'

# INCLUDE THE FORMATTING FUNCTION OVER HERE

    news_title = 'Trending News'
    articles_l = get_trending('popularity')
    sources = get_sources()
    articles = sub_arrays(articles_l, 9)
    # print(articles)
    return render_template('index.html', articles=articles, news_title=news_title, title=title, sources=sources)


# defining a route that will get the news fron a selected category
@main.route('/<cat>')
def category(cat):
    # this will be used as category title in the html
    news_title = cat.upper()
    # call get categories function which returns articles from the selected category only
    # since these articles will be displayed on the same html as popular news. i name then exactly the same so that they can just overide popular news
    articles = get_categories(cat)
    return render_template('index.html', articles=articles, news_title=news_title)


# defining a route that will get news from various sources when a source is clicked on
@main.route('/sources/<source>')
def sources(source):
    # first check if a source actually exists
    if source:
        # call a function that returns details about that specific news source
        source = get_source_details(source)
        # call function that returns articles from a gicen source
        source_articles = get_source_articles(source)
        return render_template('sources.html', articles=source_articles, source=source)

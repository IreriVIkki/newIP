# Using the defined api urls and keys to make requests
# start by importing urllib to make the requests and json to format the responses i get into json files
import urllib.request
import json
# import Sources and Articles models to create instances from the data recieved
from .models import Articles, Sources

# declaring variables to hold my api keys and api urls
# you see variables defining the keys and url are all the way outside of toen. I therefore need to bring them over. so i write a function that takes in the main app as a parameter and in it, initializes the keys variables. It also makes them global so that they can be accesses from all over the blueprint;
api_link = None
api_category = None
api_sources = None
api_onesource = None
trending_url = None
news_api_key = None


def configure_requests(app):
    global api_category, api_link, api_onesource, api_sources, trending_url, news_api_key
    api_onesource = app.config['api_onesource']
    api_category = app.config['api_category']
    api_link = app.config['api_link']
    api_sources = app.api_category['api_sources']
    trending_url = app.config['trending_url']
    news_api_key = app.config['news_api_key']


# defining a function for getting the trending news from the us that will be displayed first in the home page
def get_trending(sort):
    # format the api url adding the sort parameters and the api key
    url = api_link.format(sort, news_api_key)
    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = json.loads(data)

        # create an empty articles object that will hold the article json file
        articles = None

        # an if condition to check if the request returned any data at all
        if data['articles']:
            articles_json = data['articles']
            articles = process_articles(articles_json)

    return articles


# creating a function for getting list of articles by categories
def get_categories(category):
    # format url for calling categories api
    url = api_category.format(category, news_api_key)

    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = json.loads(data)

        # empty list that will hold the final processed lost
        articles = None

        # check if response contains a list of articles
        if data['articles']:
            articles_list = data['articles']
            articles = process_articles(articles_list)
    return articles


# defining a function for getting news from one particular source
def get_source_articles(source):
    url = api_onesource.format(source, news_api_key)

    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = json.loads(data)

        # empty artilces list to hold the final list of articles
        articles = None

        # check that the articles list is not empty
        if data['articles']:
            articles_jsonlist = data['articles']
            articles = process_articles(articles_jsonlist)

    return articles


# defining a function for getting sources data
def get_sources():
    # formatting url for getting details about news providers
    url = api_sources.format(news_api_key)

    with urllib.request.urlopen(url) as res:
        data = res.read()
        data = json.loads(data)

        sources = None
        if data['sources']:
            sources = process_sources(data['sources'])
        # print(len(sources))
    return sources


# defining a function for processing dettails about various news outlets
def process_sources(sources_list):
    # loop thorough all the sources in the list and process each one of them
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        # initialize an epty variable to hold the list of sources outlets
        sources = []

        if language == 'en':
            new_source = Sources(id, name, description, url,
                                 category, language, country)
            sources.append(new_source)
    return sources


# creating a function that takes in an articles list json file and formats it to a list of article object formated using the articles class. this function will take a list of articles json files as its parameters. This function will be reused whenever i want to format a list of article json objects
def process_articles(articles_list):
    # loop throught the list and map all the relevant information to the articles class
    for article in articles_list:
        source = article.get('source')
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        # declare an emplty list onto which the new articles objects will me appended
        articles_items = []

        # check if the article has a picture before adding it to the list of articles
        if urlToImage:
            new_article = Articles(
                id, source, author, title, description, url, urlToImage, publishedAt)
            articles_items.append(new_article)

    # return the final list of formatted articles
    return articles_items

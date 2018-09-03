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
    pass

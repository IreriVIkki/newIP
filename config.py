# import os so that I can access instance config file from the sysytem and import the api key
import os

#  create class config and set up all the api keys to be used in this project


class Config:

    # declaring Config properties that include api urls to be used
    api_link = 'https://newsapi.org/v2/top-headlines?q={}&country={}&sortBy={}&apiKey={}'
    api_category = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    api_sources = 'https://newsapi.org/v2/sources?sortBy=popularity&apiKey={}'
    api_onesource = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    trending_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    # using os to get the api key from the instance config file
    news_api_key = os.environ.get('API_KEY')


# creating a production configuration childclass with general configurations settings

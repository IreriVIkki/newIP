# import os so that I can access instance config file from the sysytem and import the api key
import os

#  create class config and set up all the api keys to be used in this project


class Config:

    # declaring Config properties that include api urls to be used
    API_LINK = 'https://newsapi.org/v2/top-headlines?country=us&sortBy={}&apiKey={}'
    API_CATEGORY = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    API_SOURCES = 'https://newsapi.org/v2/sources?sortBy=popularity&apiKey={}'
    API_ONESOURCE = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    TRENDING_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    # using os to get the api key from the instance config file
    NEWS_API_KEY = os.environ.get('API_KEY')


# creating a production configuration childclass with general configurations settings
# parent class is passed in to the childs parameters to cofirm inheritance
class ProdConfig(Config):
    pass


# Config child class that declares all the development configuration settings
# also takes in parent Config class as its argument
class DevConfig(Config):
    # in here i set debuging to true to allow for debugging features and also for the project to auto reload as I work on it
    DEBUG = True


# create a dictionary property that will be used to set configurations settings later in application
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

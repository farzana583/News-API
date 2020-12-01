import os

class Config:

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
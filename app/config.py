class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=3f6d5609132447cfa88a87c355e8253d'
    NEWS_ARTICLE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=3f6d5609132447cfa88a87c355e8253d'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
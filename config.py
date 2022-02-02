
import os
class Config:
    '''
    General configuration parent class
        '''
    NEWS_API_KEY='eb727d69c8364c9dba3a56512f487f3c'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=eb727d69c8364c9dba3a56512f487f3c'
    TEC_API_BASE_URL='https://newsapi.org/v2/everything?q=Apple&from=2022-02-02&sortBy=popularity&apiKey=eb727d69c8364c9dba3a56512f487f3c'
    # ALL_API_BASE_URL='https://newsapi.org/v2/top-headlines/sources?country=usapiKey=eb727d69c8364c9dba3a56512f487f3c'

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

config_options = {
'development':DevConfig,
'production':ProdConfig
}
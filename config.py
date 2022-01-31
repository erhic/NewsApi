
import os
class Config:
    '''
    General configuration parent class
        '''
    NEWS_API_KEY=os.environ.get('eb727d69c8364c9dba3a56512f487f3c')
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=eb727d69c8364c9dba3a56512f487f3c'


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
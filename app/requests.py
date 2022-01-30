import urllib.request,json
from .models import News

#sources

# Getting api key
api_key = None
# Getting source url
base_url= None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url= app.config['NEWS_API_BASE_URL']
    
def get_news():
    '''
    function that gets the json response to our url request
    '''
    news_url=base_url.format(api_key )
    
    with urllib.request.urlopen(news_url)as url:
        news_data=url.read()
        news_response=json.loads(news_data)
    

import urllib.request,json
from .models import News

#sources

# Getting api key
Api_key = None
# Getting source url
Base_url= None

def configure_request(app):
    global Api_key, Base_url
    Api_key = app.config['NEWS_API_KEY']
    Base_url= app.config['NEWS_API_BASE_URL']
    

    

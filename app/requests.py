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
        
        news_result=[]
        
        if news_response['articles']:
            results_list=news_response['articles']
           
            news_result=process_result(results_list)
            print(type(results_list)) 
    return news_result
   

def process_result(new_list):
    '''
    function that process news list and make the a list of objects
    '''
    news_result=[]
    for news_item in new_list:
        title=news_item.get('title')
        description=news_item.get('description')
        urlToImage=news_item.get('urlToImage')
        content=news_item.get('content')
        publishedAt=news_item.get('publishedAt')
    
        news_obj=News(title,description,urlToImage,content,publishedAt)
        
        news_result.append(news_obj)
    return news_result
    

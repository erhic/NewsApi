import urllib.request,json
from .models import News



#sources

# Getting api key
api_key = None
# Getting source url
base_url= None
# Getting source url
tech_url= None
# Getting source url
all_url= None

def configure_request(app):
    global api_key, base_url,tech_url,all_url
    api_key = app.config['NEWS_API_KEY']
    base_url= app.config['NEWS_API_BASE_URL']
    tech_url= app.config['TEC_API_BASE_URL']
    # all_url= app.config['ALL_API_BASE_URL']
    
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
        url=news_item.get('url')
        content=news_item.get('content')
        publishedAt=news_item.get('publishedAt')
    
        news_obj=News(title,description,urlToImage,url,content,publishedAt)
        
        news_result.append(news_obj)
    return news_result




def get_technews():
    '''
    function that gets the json response to our url request
    '''
    new_url=tech_url.format(api_key )
    
    with urllib.request.urlopen(new_url)as url:
        new_data=url.read()
        new_response=json.loads(new_data)
        
        new_result=[]
        
        if new_response['articles']:
            result_list=new_response['articles']
           
            new_result=process_results(result_list)
            print(type(result_list)) 
            print(new_result)
    return new_result
   

def process_results(new_list):
    '''
    function that process news list and make the a list of objects
    '''
    new_result=[]
    for new_item in new_list:
        title=new_item.get('title')
        description=new_item.get('description')
        urlToImage=new_item.get('urlToImage')
        url=new_item.get('url')
        content=new_item.get('content')
        publishedAt=new_item.get('publishedAt')
    
        news_obj=News(title,description,urlToImage,url,content,publishedAt)
        
        new_result.append(news_obj)
    return new_result

# def get_allnews():
#     '''
#     function that gets the json response to our url request
#     '''
#     news_url=all_url.format(api_key )
    
#     with urllib.request.urlopen(news_url)as url:
#         news_data=url.read()
#         news_response=json.loads(news_data)
        
#         news_result=[]
        
#         if news_response['articles']:
#             results_list=news_response['articles']
           
#             news_result=process_result(results_list)
#             print(type(results_list)) 
#     return news_result
   

# def process_result(new_list):
#     '''
#     function that process news list and make the a list of objects
#     '''
#     news_result=[]
#     for news_item in new_list:
#         title=news_item.get('title')
#         description=news_item.get('description')
#         urlToImage=news_item.get('urlToImage')
#         url=news_item.get('url')
#         content=news_item.get('content')
#         publishedAt=news_item.get('publishedAt')
    
#         news_obj=News(title,description,urlToImage,url,content,publishedAt)
        
#         news_result.append(news_obj)
#     return news_result
    

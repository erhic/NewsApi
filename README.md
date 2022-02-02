# NewsAPI 

#### Author: [Eric N](https://github.com/erhic/NewsApi)

### Description
----
    This is a website application that display the latest news from various source and sync the news after every 15 minutes to fetch latest one.It achieves this by using the News API.

### BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources |
| Display the preview of an article | **On page load** | Each article displays an image,description and publication date |
| To Read an entire article  | **Click an article** | Redirected to the news source's site to read the entire article |


### Technologies Used
----
- HTML
- PYTHON 3.8.10
- FLASK 1.1.4
- BOOTSTRAP V3

### Setup and Installion Process
----
## Prerequisites
* python3.8.10
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/erhic/NewsApi
        $ cd NewsApi

## Running the Application
* Creating the virtual environment

        $ python3 -m venv --without-pip virtual
      
        
* Installing Flask and other Modules

        $ pip install Flask
        $ pip install Flask-Bootstrap
        $ pip install Flask-Script

* Setting up the API Key


        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh and place your API key here together with the command to run the server.


* To run the application, in your terminal:

        $  chmod +x start.sh 
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3 manage.py tests


### Support and Contact Details
----
For feedback or any information pertaining this project feel free to reach me through :

Email: ericngugi24@gmail.com

### Licence 
---
 [ LICENCE](LICENCE) 
 (link to MIT License )
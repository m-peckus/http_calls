#!/usr/bin/env python3

# Import modules
from newsapi import NewsApiClient
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Access API key from .env file
API_KEY = os.getenv('API_KEY')

# Init
newsapi = NewsApiClient(API_KEY)

# GET endpoint to News API
base_url = f"https://newsapi.org/v2/everything?q=Apple&from=2025-01-01&sortBy=popularity&apiKey={API_KEY}"

url = "https://newsapi.org/v2/top-headlines"

params ={
    'country': 'us', # Change the country to use a different endpoint
    'apiKey': API_KEY
}

response = requests.get(url, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json() # Parse json data

    # Extract articles from json response
    articles = data['articles']

    # Print the titles and descriptions of articles
    for i, article in enumerate(articles, 1):
        title = article['title']
        description = article['description']
        url = article['url']
        print(f"{i}. {title}\n Description: {description}\n URL: {url}\n")
else:
    print("Error: Unable to fetch data")

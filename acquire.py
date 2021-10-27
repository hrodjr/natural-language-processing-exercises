
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import strftime

def blog_links():
    url = 'https://codeup.com/blog/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    urls = [links.attrs['href'] for links in soup.select('.entry-featured-image-url')]
    
    return urls

def article(url):
    url = 'https://codeup.com/blog/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    
    return {
        'title':soup.select_one('.entry-title').text,
        'content':soup.select_one('.post-content-inner').text.strip(),
    }

def get_blog_articles():
    links = blog_links()
    df = pd.DataFrame([article(url) for link in links])
    return df


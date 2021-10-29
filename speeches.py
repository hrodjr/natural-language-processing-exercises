from bs4 import BeautifulSoup
import pandas as pd
from requests import get
import unicodedata
import re
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


def president_links(url):
    response = get(url, headers = {'User-Agent': 'Codeup Data Science'})
    soup = BeautifulSoup(response.text, features="lxml")
    urls = [links.attrs['href'] for links in soup.select('.full-link')]
    
    return urls

def acquire_speech(url):
    response = get(url, headers = {'User-Agent': 'Codeup Data Science'})
    soup = BeautifulSoup(response.text, features='lxml')
    speech = soup.select('.body-content')
    speech = speech[0].select('p')
    words = [words.text for words in speech]
    
    return words

def acquire_speech_avalon(url):
    response = get(url, headers = {'User-Agent': 'Codeup Data Science'})
    soup = BeautifulSoup(response.text, features='lxml')
    speech = soup.select('.text-properties')
    speech = speech[0].select('p')
    words = [words.text for words in speech]
    
    return words

def clean_speech(words):
    original = ' '.join(words)
    text = original.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r"[^a-z0-9'\s]", '', text)
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text_lemma = ' '.join(lemmas)
    stopwords = nltk.corpus.stopwords.words('english')
    newStopWords = ['u','ha','wa']
    stopwords.extend(newStopWords)
    words = text_lemma.split()
    filtered_words = [w for w in words if w not in stopwords]
    speech = ' '.join(filtered_words)

    return speech

def all_presidents(url):
    response = get(url, headers = {'User-Agent': 'Codeup Data Science'})
    soup = BeautifulSoup(response.text, features='lxml')
    speech = soup.select('.body-content')
    speech = speech[0].select('p')
    words = [words.text for words in speech]
    original = ' '.join(words)
    text = original.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r"[^a-z0-9'\s]", '', text)
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    text_lemma = ' '.join(lemmas)
    stopwords = nltk.corpus.stopwords.words('english')
    newStopWords = ['u','ha','wa']
    stopwords.extend(newStopWords)
    words = text_lemma.split()
    filtered_words = [w for w in words if w not in stopwords]
    speech = ' '.join(filtered_words)
    img = WordCloud(background_color='white').generate(speech)
# WordCloud() produces an image object, which can be displayed with plt.imshow
    plt.imshow(img)
# axis aren't very useful for a word cloud
    plt.axis('off')
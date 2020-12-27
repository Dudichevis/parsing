from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

pythonist = 'https://pythonist.ru/category/topnews/'
habr = 'https://habr.com/ru/hub/programming/'
unetway = 'https://unetway.com/blog'

pythonist_list = []
habr_list = []
unetway_list = []


def news_pythonist():
    page = requests.get(pythonist)
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.find_all('article')
    for post in news:
        title = post.find('h2', class_= 'entry-title').text
        url = post.find('a').get('href')
        data = {'title': title, 'url': url}
        pythonist_list.append(data)




def news_habr():
    page = requests.get(habr)
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.find_all('article')
    for post in news:
        title = post.find('a', class_='post__title_link').text
        url = post.find('a', class_='post__title_link').get('href')
        data = {'title': title, 'url': url}
        habr_list.append(data)


def news_unetway():
    page = requests.get(unetway)
    soup = BeautifulSoup(page.text, 'html.parser')
    news = soup.find_all('article', class_='blog-block')
    for post in news:
        title = post.find('h2').text
        url = post.find('a').get('href')
        data = {'title': title, 'url': url}
        unetway_list.append(data)


news_pythonist()
news_habr()
news_unetway()


def news_home(request):
    template = 'news_app/index.html'
    context = {
        'unetway_list': unetway_list,
        'habr_list': habr_list,
        'pythonist_list': pythonist_list,
    }
    return render(request, template, context)

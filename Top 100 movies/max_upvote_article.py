from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

article_texts = []
article_links = []

article = soup.find_all(name='a', class_='storylink')
for article_tag in article:
    text = article_tag.text
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.text.split(' ')[0]) for score in soup.find_all(name='span', class_='score')]
index_max_upvotes = article_upvotes.index(max(article_upvotes))

print(article_texts[index_max_upvotes])
print(article_links[index_max_upvotes])

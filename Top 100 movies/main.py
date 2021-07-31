import requests
from bs4 import BeautifulSoup

empire_url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(f'http://web.archive.org/web/20200518055830/{empire_url}')
soup = BeautifulSoup(response.text, 'lxml')

top_movies = soup.find_all(name='h3', class_='title')
movie_list = [movie.text for movie in top_movies]

with open('top-movies.txt', 'w', encoding='UTF-8') as file:
    for item in movie_list[::-1]:
        file.write(f'{item}\n')

from bs4 import BeautifulSoup
import requests
import lxml
import re

movies_list_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(movies_list_url)
movie_site_text = response.text

soup = BeautifulSoup(movie_site_text,"lxml")

title_anchor = soup.find_all(name="h3", class_="title")
titles = []
#delimiters = r'[):]'
# for title in title_anchor:
#     single_title = title.getText()
#     single_title = single_title.replace('â\x80\x93', "")
#     single_title = re.split(delimiters,single_title)[1]
#     titles.append(single_title)
movie_titles = [movie.getText().replace('â\x80\x93', "") for movie in title_anchor]


#titles = titles[::-1]
movie_titles = movie_titles[::-1]
#print(titles)
with open("movies.txt","w") as file:
    for movie in movie_titles:
        file.write(movie + "\n")

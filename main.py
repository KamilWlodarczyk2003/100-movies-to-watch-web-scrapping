from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

list_of_movie_line = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movies = [movie.getText() for movie in list_of_movie_line]
movies.reverse()

with open("movies.txt", "w") as file:
    for movie in movies:
        file.writelines(f"{movie}\n")
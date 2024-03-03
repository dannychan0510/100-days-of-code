from bs4 import BeautifulSoup
import requests

# URL of the webpage to scrape
url = "https://www.empireonline.com/movies/features/best-movies-2/"
# archived_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL and retrieve the webpage content
r = requests.get(url)

# Extract the HTML content from the response
website = r.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(website, "html.parser")

# Find all the movie titles on the webpage and store them in a list
top_100_movies = [movie.text for movie in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")]
top_100_movies.reverse()

# Write the movie titles to a file in reverse order
with open("./day-45-web-scraping/movies.txt", mode="w") as file:
    for movie in top_100_movies:
        file.write(movie + "\n")

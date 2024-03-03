from bs4 import BeautifulSoup
import requests

# Send a GET request to the website
response = requests.get("https://news.ycombinator.com/news")

# Get the HTML content of the webpage
yc_webpage = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(yc_webpage, "html.parser")

# Extract the text of each article
article_texts = [x.find('a').getText() for x in soup.find_all('span', class_='titleline')]

# Extract the links of each article
article_links = [x.find('a').get('href') for x in soup.find_all('span', class_='titleline')]

# Extract the upvotes count of each article
article_upvotes = [int(x.getText().split()[0]) for x in soup.find_all('span', class_='score')]

# Find the largest upvote count
largest_upvote = max(article_upvotes)

# Find the index of the article with the largest upvote count
largest_upvote_idx = article_upvotes.index(largest_upvote)

# Get the text of the article with the largest upvote count
largest_upvote_article = article_texts[largest_upvote_idx]

# Print the article with the largest upvote count
print(largest_upvote_article)

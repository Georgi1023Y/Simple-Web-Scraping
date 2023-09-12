import requests
from bs4 import BeautifulSoup

# Enter the url of the website you want to scrape.
url = 'url'
# Make get request.
response = requests.get(url)

# Create beautiful soup object
soup = BeautifulSoup(response.text, 'html.parser')

# Getting all of the links from the scraped website
for link in soup.find_all('a'):
    print(link.get('href'))

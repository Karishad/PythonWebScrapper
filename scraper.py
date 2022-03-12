# scraper.py
# Ensure beautifulsoup is installed prior to running

# Beautiful Soup is going to be our web scrapper
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# sudo apt update
# pip install beautifulsoup4

# Requests is going to allow use to send HTTP requests to the webpages that we scrape
# https://docs.python-requests.org/en/latest/
# sudo apt update
# pip install requests

from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Main_Page"
request = requests.Request(url)
soup = BeautifulSoup(request.text, "html.parser")
print(soup.title)

# scraper.py

# Beautiful Soup is going to be our web scrapper
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Requests is going to allow use to send HTTP requests to the webpages that we scrape
# https://docs.python-requests.org/en/latest/

# tkinter is going to allow the creation of the GUI for the webscrapper
# https://docs.python.org/3/library/tkinter.html

from bs4 import BeautifulSoup
import requests
import tkinter as tk

# setting up the GUI
root = tk.Tk()
message = tk.Label(root, text="Hello, World!")
message.pack()
root.mainloop()

# url to scrape
url = "https://en.wikipedia.org/wiki/Main_Page"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
print(soup.title.text)


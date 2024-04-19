import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.startupreporter.eu/burning-heroes-startup-competition-in-london/")
soup = BeautifulSoup(r.text, "html.parser")
titles = soup.find_all("header", attrs={"class": "cf"})
date = soup.find("span",attrs={"class":"date"})
texts = soup.find("div",attrs={"class":"content cf"})

for new in titles:
    if not new.h1 is None:
        print(new.h1.text)

print(date.text)
print(texts.text)

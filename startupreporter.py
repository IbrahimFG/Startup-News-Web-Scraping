import requests
from bs4 import BeautifulSoup

page_number = 1
while True:
    r = requests.get(f"https://www.startupreporter.eu/category/startups/page/{page_number}/")
    page_number += 1
    if r.status_code != 200:
        break

    soup = BeautifulSoup(r.text, "html.parser")
    titles = soup.find_all("header", attrs={"class": "cf"})
    article_div = soup.find("div", attrs={"id": "content"})
    links = article_div.find_all("article")

    for link in links:
        print(link.a['href'])

    for new in titles:
       if not new.h1 is None:
            print(new.h1.text)




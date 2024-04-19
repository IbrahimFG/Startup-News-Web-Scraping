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
        r = requests.get(link.a['href'])
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.find_all("header", attrs={"class": "cf"})
        date = soup.find("span",attrs={"class":"date"})
        texts = soup.find("div",attrs={"class":"content cf"})

        for t in title:
            if not t.h1 is None:
                print(t.h1.text)

        print(date.text)
        print(texts.text)
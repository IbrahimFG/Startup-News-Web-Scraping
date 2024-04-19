import requests
from bs4 import BeautifulSoup


page_number = 1
while True:
    r = requests.get(f"https://www.20minutos.es/minuteca/startups/{page_number}/")
    page_number += 1
    soup = BeautifulSoup(r.text, "html.parser")
    news = soup.find_all("article",attrs={"class":"media"})

    for new in news:
        print(new.h1.text)
        print(new.a['href'])
        response = requests.get(new.a["href"])
    if r.status_code != 200:
        break

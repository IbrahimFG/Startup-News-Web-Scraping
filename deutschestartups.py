import requests
from bs4 import BeautifulSoup


page_number = 1
while True:
    r = requests.get(f"https://www.deutsche-startups.de/ressort/startups/page/{page_number}/")
    page_number += 1
    soup = BeautifulSoup(r.text, "html.parser")
    news = soup.find_all("div",attrs={"class":"post"})

    for new in news:
        print(new.h3.text)
        print(new.a['href'])
        response = requests.get(new.a["href"])
    if r.status_code != 200:
        break

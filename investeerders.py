import requests
from bs4 import BeautifulSoup


page_number = 1
while True:
    r = requests.get(f"https://www.investeerders.nl/nieuws/page/{page_number}/")
    page_number += 1
    soup = BeautifulSoup(r.text, "html.parser")
    titles = soup.find_all("a",attrs={"class":"hover:text-brand-500"})

    for title in titles:
        print(title.text)
    if r.status_code != 200:
        break
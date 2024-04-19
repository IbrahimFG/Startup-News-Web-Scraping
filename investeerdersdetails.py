import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.investeerders.nl/instroom-europese-bitcoin-etns-langzaam-op-gang/")
soup = BeautifulSoup(r.text, "html.parser")
title = soup.find("h1",attrs={"class":"title flex flex-wrap items-center space-between mb-2"})
date = soup.find("div",attrs={"class":"text-gray-500 text-sm md:text-base"})
texts = soup.find("div",attrs={"class":"content mb-6 no-last-child-margin"})

print(title.text)
print(date.text)
print(texts.text)

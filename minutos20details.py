import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.20minutos.es/noticia/5216504/0/record-startups-cataluna-llegan-las-2-102-2023/")
soup = BeautifulSoup(r.text, "html.parser")
title = soup.find("h1",attrs={"class":"article-title"})
date = soup.find("span",attrs={"class":"article-date"})
author = soup.find("span",attrs={"class":"article-author"})
summary = soup.find("div",attrs={"class":"article-intro trk-relacionada-bolos"})
texts = soup.find_all("p",attrs={"class":"paragraph"})

print(title.text)
print(date.text)
print(author.text)
content = summary.text
for her in texts:
    content += her.text
print(content)







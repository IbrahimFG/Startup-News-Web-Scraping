import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.deutsche-startups.de/2024/04/18/neue-startups-bitteiler-axontic/")
soup = BeautifulSoup(r.text, "html.parser")
title = soup.find_all("div",attrs={"class":"postHead"})
author = soup.find("div",attrs={"class":"meta"})
summary = soup.find("div",attrs={"class":"excerpt"})
texts = soup.find("div",attrs={"class":"wysiwyg"})


for new in title:
    if not new.h1 is None:
        print(new.h1.text)
print(author.text)
content = summary.text
for her in texts:
    content += her.text
print(content)

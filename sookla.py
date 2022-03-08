import re
from bs4 import BeautifulSoup
import requests

url = "http://192.168.22.172/menu-example/"

sisu = requests.get(url)
doc = BeautifulSoup(sisu.text, "html.parser")


#leiame general info htmlist
info = doc.find_all("h2")
#html parent branch
parent = info[2].parent
#loop et leida contents ehk sook,hind,lisainfo
stats = [
    (i.contents[0], i.contents[3].text, i.contents[1].text) for i in parent
]

print(stats[0][1])

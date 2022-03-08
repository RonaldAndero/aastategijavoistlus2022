from bs4 import BeautifulSoup
import requests
import json


url = "http://192.168.22.172/menu-example/"

sisu = requests.get(url)
doc = BeautifulSoup(sisu.text, "html.parser")

# for loop mis leiab pealkirjad, nimetused, hinnad ja lisainfod
pealkirjad = doc.select('strong')
for pealkiri in pealkirjad:
    tabel = pealkiri.findNext("ul")
    if tabel:
        asi = tabel.find_all("li")
        for rida in asi:
            stats = [
                (i.contents[0], i.contents[1].text, i.contents[3].text) for i in rida
           ]
    data = {"nimetus":pealkiri.text, "toidud": [{"nimetus": stats[0][0], "hind": stats[0][1], "lisainfo": stats[0][2]}]}
    print(data)
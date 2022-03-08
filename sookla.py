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
        print(pealkiri.text)
        asi = tabel.find_all("li")
        for rida in asi:
            stats = [
                (i.contents[0], i.contents[1].text, i.contents[3].text) for i in rida
            ]
            print(stats[0][0])
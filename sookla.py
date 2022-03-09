from bs4 import BeautifulSoup
import requests
import json

url = "http://192.168.22.172/menu-example/"


data = requests.get(url)
doc = BeautifulSoup(data.text, "html.parser")

#info jaoks list
jsonlist = []

#main kood
iterator = 0
pealkirjad = doc.select('strong')
#vaatame pealkirja järgi järest
for pealkiri in pealkirjad:
    #leiame iga ul sourcist
    tabel = pealkiri.findNext("ul")
    try:
        tabel2 = tabel.find_next_sibling()
        if tabel2 != None:
            tabel.append(tabel2)
    except:
        pass
    #kui leiame
    if tabel:
        #li sees on info
        asi = tabel.find_all("li")
        jsonlist.append({"nimetus":pealkiri.text, "toidud": []})
        #saame selle info siin
        for rida in asi:
            #kiire loop mis filtreerib infot mida meil vaja
            stats = [
                (i.contents[0], i.contents[1].text, i.contents[3].text) for i in rida
           ]
            #lükkame info listi
            jsonlist[iterator]["toidud"].append({"nimetus": stats[0][0], "hind": stats[0][1].replace("€", ""), "lisainfo": stats[0][2]})
        iterator += 1

#teeme jsoni
prettyjson = json.dumps(jsonlist, indent=4)
f = open("menu.json", "w" )
f.write(prettyjson)
f.close()
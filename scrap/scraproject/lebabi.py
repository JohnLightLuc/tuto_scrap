url = "https://www.lebabi.net/"


import json
import requests
from bs4 import BeautifulSoup

site = "https://www.lebabi.net"
cat = "/cotedivoire/"
url = '{}{}'.format(site,cat)
response = requests.get(url)
#print(response.status_code)

if response.status_code ==200:
    
    # -------------------- Recuperation html ------------------------------------- #
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # -------------------- Recuperation titre ------------------------------------- #
    ul_head = html_soup.find('ul', attrs={'id': 'menu-primary-navigation'})
    #li_head = ul_head.findAll('li')








def recupCat(url):
    import json
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.lebabi.net/"
    response = requests.get(url)
    #print(response.status_code)

    if response.status_code ==200:
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # -------------------- Recuperation titre ------------------------------------- #
        ul_head = html_soup.find('ul', attrs={'id': 'menu-primary-navigation'})
        li_head = ul_head.findAll('li')
        categorie = []
        for item in li_head:
            mydict = dict()
            nom = item.text
            url = item.a['href']
            mydict["nom"] = nom
            mydict["url"] = url
            categorie.append(mydict)
        categorie.pop(0)
        categorie = json.dumps(categorie)

        return categorie

#print(recupCat(url = "https://www.lebabi.net/"))
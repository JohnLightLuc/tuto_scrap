url = "https://www.lebabi.net/"
url_cat = "/cotedivoire/"
detail = "/actualite/dossier-gbagbo-ble-goude-a-la-cpi-affi-veut-rencontrer-ouattara-la-reponse-du-chef-de-l-etat-85385.html"



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


def recupCatArticles(url_cat):
    import json
    import requests
    from bs4 import BeautifulSoup

    site = "https://www.lebabi.net"
    
    url = '{}{}'.format(site,url_cat)
    response = requests.get(url)
    #print(response.status_code)
    myarticles = []
    if response.status_code ==200:
        
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        main = html_soup.find('div', attrs={'class': 'main col-md-8 col-xs-12'})
       
        # -------------------- Recuperation Post principal ------------------------------------- #
        post_principale = main.find('div', attrs={'class': 'post'})
        titre = post_principale.find('a').text
        lien_art = post_principale.find('a')["href"]
        main_image = post_principale.find('img')["src"]
        post_content = main.find('div', attrs={'class': 'post-content'})
        date_pub = post_content.find('span').text
        date_pub = date_pub[:10]
        sort_descript = post_content.find("p").text
        # -------------Enregidtrement ---------- #
        mydict = dict()
        mydict['lien_article'] = lien_art
        mydict['image'] = main_image
        mydict['date_pub'] = date_pub
        mydict['title'] = titre
        mydict['description'] = sort_descript
        myarticles.append(mydict)
        
        # -------------------- Recuperation Des POST ------------------------------------- #
        
        team = main.find('div', attrs={'class': 'team-row'})
        articles = team.findAll('div', attrs={'class': 'col-md-6'})
        
        for article in articles:
            art = dict()
            lien_article = article.a['href']
            image = article.img["src"]
            date_pub = article.find('span').text
            date_pub = date_pub[:10]
            title = article.find('h4', attrs={'class': 'news-title'}).text
            description = article.find('div', attrs={'class': 'txtpp'}).text
            # -------------------- Enregistrement des articles ------------------------------------- #
            art['lien_article'] = lien_article
            art['image'] = image
            art['date_pub'] = date_pub
            art['title'] = title
            art['description'] = description
            myarticles.append(art)

    myarticles = json.dumps(myarticles)
    return  myarticles

def recupArticleDetail(url_article):
    import json
    import requests
    from bs4 import BeautifulSoup
    site = "https://www.lebabi.net"
    url_detail = "/actualite/dossier-gbagbo-ble-goude-a-la-cpi-affi-veut-rencontrer-ouattara-la-reponse-du-chef-de-l-etat-85385.html"
    url = "{}{}".format(site,url_detail)
    response = requests.get(url)
    article = dict()
    if response.status_code ==200:
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        main_page = html_soup.find('div', attrs={'class': 'main col-md-8 col-xs-12'})
        # -------------------- Recuperation d'info ------------------------------------- #

        tag = main_page.find('h2', attrs={'class': 'lined_une'}).text
        source = main_page.find('div', attrs={'class': 'post-meta'}).text
        source = source[46:]
        mytitre = main_page.find('h1', attrs={'class': 'post-title'}).text
        content = main_page.find('div', attrs={'class': 'post-content'})
        image = content.img["src"]
        image_descrip = content.find('span').text
        image_descrip = image_descrip[17:]
        description = main_page.find('p').text
        content = main_page.findAll('p')
        content.pop(0)
        auteur = content[-1]
        auteur = auteur.text
        content.pop(-1)
        img = dict()
        img["url"] = image
        img["description"] = image_descrip
        # -------------------- Enregistrement ------------------------------------- #

        article["titre"] = mytitre
        article["image"] = img
        article["description"] = description
        article["content"] = content
        article["auteur"] = auteur
        article["tag"] = tag
        article["source"] = source
    #article = json.dumps(article)
    return article


#print(recupCat(url = "https://www.lebabi.net/"))
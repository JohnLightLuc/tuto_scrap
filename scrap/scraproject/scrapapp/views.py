from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#192.168.50.31

def recup_categorie(url):
    
    import json
    import requests
    from bs4 import BeautifulSoup

    categories = []
    response = requests.get(url)
    #print(response.status_code)

    if response.status_code ==200:
    
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # -------------------- Recuperation titre ------------------------------------- #
        navbar = html_soup.find('nav', attrs={'id': 'navbarResponsive'})
        nav_ul = navbar.find('ul', attrs={'id': 'menu-menu-superieur'})
        cats = nav_ul.findAll('li')
        
        for item in cats:
            cat = dict()
            nom_cat = item.find('a').text
            url_cat = item.a["href"]
            cat["nom"] = nom_cat
            cat["url"] = url_cat
            categories.append(cat)
    
    categories = json.dumps(categories)

    return categories


def recupInfoArticles(url):
    import json
    import requests
    from bs4 import BeautifulSoup
    
    response = requests.get(url)
    

    if response.status_code ==200:
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # -------------------- Recuperation d'info article ------------------------------------- #
        articles_section = html_soup.find('div', attrs={'class': 'newscast-left'})
        articles = articles_section.findAll('article')
        myarticles = []
        for item in articles:
            art = dict()
            article_url = item.a["href"]
            image_url = item.img["src"]
            titre = item.find('h2').text
            
            # -------------------- Enregistrement d'info article ------------------------------------- #
            art["titre"] = titre
            art["article_url"] = article_url
            art["image_url"] = image_url
            myarticles.append(art)
    myarticles = json.dumps(myarticles) 

    return myarticles


def recupDetailArticle(url):
    import json
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)
    #print(response.status_code)
    detail_article = list()
    content = dict()
    if response.status_code ==200:
        info_site = dict()
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # -------------------- Recuperation info article  ------------------------------------- #
        navbar = html_soup.find('div', attrs={'class': 'newscast-left'})
        article_head = navbar.find('div', attrs={'class': 'header-post'})
        titre = article_head.find('h1').text
        span = article_head.find('span', attrs={'class': 'author vcard'})
        info_site["nom"]= span.text
        info_site["url"]= span.a["href"]
        date_up = article_head.find('div', attrs={'class': 'info_article'}).text
        date_update = date_up[31:]

        # -------------------- Recuperation contenu  ------------------------------------- #

        contenu = str(html_soup.find('article'))

        # -------------------- Enregistrement   ------------------------------------- #

        content["site"] = info_site
        content["date_update"] = date_update
        content["contenu"] = contenu
        detail_article.append(content)

    detail_article = json.dumps(detail_article)

    return detail_article

def categories(requests):
    categories = recup_categorie(url = "https://www.7info.ci/")
    return HttpResponse(categories)


def articles(requests):
    data = recupInfoArticles(url = "https://www.7info.ci/category/ntic/")
    return HttpResponse(data)

def detail(requests):
    data = recupDetailArticle(url = "https://www.7info.ci/cyberphone-un-telephone-indestructible-sur-le-marche/")
    return HttpResponse(data)


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

def singles(requests):
    detail = "/actualite/dossier-gbagbo-ble-goude-a-la-cpi-affi-veut-rencontrer-ouattara-la-reponse-du-chef-de-l-etat-85385.html"
    data = recupArticleDetail(detail)
    return HttpResponse(data)

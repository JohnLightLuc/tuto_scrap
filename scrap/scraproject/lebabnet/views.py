from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import Article
# Create your views here.

url = "https://www.lebabi.net/"
url_cat = "/cotedivoire/"
detail = "/actualite/dossier-gbagbo-ble-goude-a-la-cpi-affi-veut-rencontrer-ouattara-la-reponse-du-chef-de-l-etat-85385.html"



##################### OBTENIR LES GROUPEMENTS DES ARTICLES ##################        
    
def recupCat():
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

##################### OBTENIR LES ARTICLES D'UN GROUPEMENTS ##################

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

##################### OBTENIR LES ARTICLES ET LEUR CATEGORIE ##################

def getAllArticles():
    import json
    import requests 
    from bs4 import BeautifulSoup

    url = "https://www.lebabi.net/cotedivoire/"
    response = requests.get(url)


    if response.status_code ==200:
        
        # -------------------- Declaration des variables ------------------------------------- #
        myarticles = list()
        myarticle = dict()
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # -------------------- Recuperation des articles------------------------------------- #
        all_articles = html_soup.find('div', attrs={'id': 'toutes-les-articles'})
        articles = all_articles.findAll('div', attrs={'class': 'articles'})
        
        for article in articles:
            print(article)
            url_article = article.a["href"]
            cat_article = article.find('span').text
            h4 = article.find('h4', attrs={'class':'list-title'})
            titre = h4.find('a').text
            image = article.img["src"]
            descript = article.find('p').text

            myarticle['titre'] = titre
            myarticle['categorie'] = cat_article
            myarticle['url'] = url_article
            myarticle['description'] = descript
            myarticle['image'] = image

            myarticles.append(myarticle)

    return myarticles


##################### OBTENIR ARTICLE PAR GROUPEMENTS ##################

def recupArticleDetail(url_article):
    import json
    import requests
    from bs4 import BeautifulSoup
    site = "https://www.lebabi.net"
    #url_detail = "/actualite/dossier-gbagbo-ble-goude-a-la-cpi-affi-veut-rencontrer-ouattara-la-reponse-du-chef-de-l-etat-85385.html"
    url = "{}{}".format(site,url_article)
    response = requests.get(url)
    my_article = list()
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
        my_article.append(article)
    #article = json.dumps(article)
    return my_article       


def articles(requests):
    myarticles = list(getAllArticles())
    
    i = 1
    for article in myarticles:
        try:
           
            # new_Article = Article()
            # new_Article.titre = article["titre"]
            # new_Article.categorie = article["categorie"]
            # new_Article.url_article = article["url"] 
            # new_Article.image_min = article["image"] 
            # new_Article.description = article["description"] 
            

            # detail = list(recupArticleDetail(article["url"]))
            # print(detail)
            # detail = detail[0]
            # new_Article.image_max = detail['image']["url"]
            # new_Article.contenu = detail['content']
            # new_Article.save()
            #print(i,article)
            i = i +     1
        except:
            print("Erroor")
        


    myarticles = json.dumps(myarticles)

    return HttpResponse(myarticles)
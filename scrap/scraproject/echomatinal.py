
def getCategories():
    import json
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.echomatinal.com/"

    response = requests.get(url)
    #print(response.status_code)
    categories = []
    if response.status_code ==200:
        
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # -------------------- Recuperation titre ------------------------------------- #
        navbar = html_soup.find('ul', attrs={'id': 'menu-primary-menu' })
        items = navbar.findAll('li')
        categories = []
        for item in items:
            cat = dict()
            nom_cat = item.find('a').text
            lien_cat = item.a['href']
            cat['nom'] = nom_cat
            cat['url'] = lien_cat
            categories.append(cat)
    categories = json.dumps(categories)

    return categories

def getAllCatArticles(url_cat):
    import json
    import requests
    from bs4 import BeautifulSoup
    
    #url = "https://www.echomatinal.com/economie/"
    response = requests.get(url_cat)

    all_articles = list()
    if response.status_code ==200:
        
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        pagination = html_soup.find('div', attrs={'class': 'pagination' })
        a_all = pagination.findAll('a')
        a = a_all[-1]
        last_url = a["href"]
        page_num = last_url.split('/')
        page_num = page_num[-2]
        try:
            page_num = int(page_num)
        except:
            page_num = 0
        if page_num != 0:
            
            for i in range(1, page_num):
                html_soup = BeautifulSoup(response.text, 'html.parser')
                content = html_soup.find('div', attrs={'class': 'main-col' })
                articles = content.findAll('div', attrs={'class': 'default-blog-post' })
                my_article = dict()
                for article in articles:
                    #------------ Titre ------------------------
                    h2 = article.find('h2')
                    titre = h2.text
                    #------------ Update ------------------------
                    date_update = article.find('span').text
                    date_update = date_update[4:]
                    #------------ Lien article ------------------------
                    lien_art = h2.a["href"]

                    #------------ Lien image ------------------------
                    detail = article.find('div', attrs={'class': 'bp-details' })
                    url_image = detail.img["src"]
                    #------------ Descritpon ------------------------
                    description = detail.find('p').text

                    #------------ Enregistrement article ------------------------
                    my_article["titre"] = titre
                    my_article["date_update"] = date_update
                    my_article["detail"] = lien_art
                    my_article["image"] = url_image
                    my_article["description"] = description

                    all_articles.append(my_article)

    all_articles = json.dumps(all_articles)
    return all_articles
                

import json
import requests
from bs4 import BeautifulSoup

url = "https://www.echomatinal.com/reforme-du-franc-cfa-creation-de-leco-les-grandes-decisions-prises-au-56eme-sommet-de-la-cedeao-a-abuja/"

response = requests.get(url)
#print(response.status_code)
categories = []
if response.status_code ==200:
    
    # -------------------- Recuperation html ------------------------------------- #
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # -------------------- Recuperation titre ------------------------------------- #
    navbar = html_soup.find('div', attrs={'class': 'bp-horizontal-share' })
            

   
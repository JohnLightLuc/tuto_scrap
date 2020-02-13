url = "https://www.7info.ci/"
url ='https://www.7info.ci/category/politique/'
url = 'https://www.7info.ci/soro-ne-decroche-pas-son-telephone-a-paris/'




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
    typ = type(categories)
    return typ


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

def getCatArticles(url):
    catArticles = recupInfoArticles(url)
    articles = list()
    for item in catArticles:
        url_art = item["article_url"]
        article = recupDetailArticle(url_art)
        articles.append(article)
    return article
#print(recup_categorie(url = "https://www.7info.ci/"))
var = recupInfoArticles(url = "https://www.7info.ci/category/eco-business/")
#print(var)
#print(recupDetailArticle(url = "https://www.7info.ci/la-cci-ci-initie-un-cadre-dechange-entre-les-entreprises-et-les-pouvoirs-publics/"))

#print(getCatArticles(url = "https://www.7info.ci/category/eco-business/"))

catArticles = recupInfoArticles(url = "https://www.7info.ci/category/eco-business/")
#print(type(catArticles))
articles = list()
#for item in catArti    cles:
    #url_art = item["article_url"]
print("#############################################")

print(recup_categorie(url = "https://www.7info.ci/"))

print("#############################################")
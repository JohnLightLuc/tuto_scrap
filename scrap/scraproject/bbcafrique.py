
#https://www.bbc.com/afrique

def getCategories(url):
    ####### import ########
    import requests
    from bs4 import BeautifulSoup

    #url = "https://www.bbc.com/afrique"
    response = requests.get(url)
    categories = []

    if response.status_code ==200:
       
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        
        # -------------------- Recuperation d'elements de bare navigation ------------------------------------- #
        div_nav = html_soup.find('div', attrs={'class': 'navigation navigation--wide'})
        ul_items = div_nav.find('ul')
        elements = ul_items.findAll('li')

        # -------------------- Recuperation des Categories et url ------------------------------------- #
        
        for items in elements:
            mondic = dict()
            nom = items.find('span').text
            a = items.find('a')
            url = a['href']
            mondic["nom"] = nom
            mondic["url"] = url
            categories.append(mondic)
        return categories
        
    else:
        return categories

url = "https://www.bbc.com"
categorie = "/afrique/region"

def articles(url, categorie):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get("{}{}".format(url, categorie))

    articles = []

    if response.status_code ==200:
    
        # -------------------- Recuperation html ------------------------------------- #
        html_soup = BeautifulSoup(response.text, 'html.parser')
        main_page = html_soup.find('div', attrs={'role': 'main'})
        div_container = main_page.find('div', attrs={'class': 'container'})
        div_eagle = div_container.find('div', attrs={'class': 'eagle'})
        article_sections = div_eagle.findAll('div', attrs={'class': 'eagle-item faux-block-link'})
        i = 0
        for item in article_sections:
            article = dict()
            i = i+1
            # -------------------- Recuperation url image ------------------------------------- #
            imagesection = item.find('div', attrs={'class': 'eagle-item__image'})
            div_response = imagesection.find('div', attrs={'class': 'responsive-image'})
            try:
                img_url = div_response.div["data-src"]
            except:
                img_url =""
            
        
            # -------------------- Recuperation info artile ------------------------------------- #
            infosection = item.find('div', attrs={'class': 'eagle-item__body'})
            a = infosection.find('a')
            url_article = a['href']
            titre_article = infosection.find('h3', attrs={'class': 'title-link__title'}).text
            descrip_article = infosection.find('p', attrs={'class': 'eagle-item__summary'}).text
            date_add = infosection.find('ul', attrs={'class': 'mini-info-list'}).text

            # -------------------- Enregistrer artile ------------------------------------- #
            
            article["img_url"] = img_url
            article["url_article"] = url_article
            article["titre_article"] = titre_article
            article["descrip_article"] = descrip_article
            article["date_add"] = date_add
            
            articles.append(article)
            
        

        print("###################################")
   
    return articles







####### import ########
import requests
from bs4 import BeautifulSoup

#url = "https://www.bbc.com/afrique"
response = requests.get(url)
categories = []
url = "https://www.bbc.com"
urlArticle ="/afrique/region-51444841"

response = requests.get("{}{}".format(url, urlArticle))

if response.status_code ==200:

    # -------------------- Recuperation html ------------------------------------- #
    html_soup = BeautifulSoup(response.text, 'html.parser')
    main_page = html_soup.find('div', attrs={'role': 'main'})
    div_container = main_page.find('div', attrs={'class': 'container'})
    info_article = div_container.find('div', attrs={'class': 'story-body'})
    print(info_article)




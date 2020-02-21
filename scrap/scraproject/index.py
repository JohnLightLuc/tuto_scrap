import requests
from bs4 import BeautifulSoup

url = "http://www.abidjanguide.com/"
response = requests.get(url)
#print(response.status_code)

if response.status_code ==200:
    # -------------------- Recuperation html ------------------------------------- #
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # -------------------- Recuperation titre ------------------------------------- #
    div_title = html_soup.find('div', attrs={'class': 'navbar-header'})
    h1_title = html_soup.find('h1')
    # -------------------- Recuperation presentation ------------------------------------- #
    div_presentaton = html_soup.findAll('div', attrs={'class': 'col-md-2'})
    # --------------------- Recuperation des services(logements, medecins, reparateur ) ----------------------------- #
    compt = 0
    for item in div_presentaton:
      if compt < 3:
        ba = item.find('a')
        url = ba['href']
        img = ba.find('img')
        h3 = ba.find('h3')
        image = img['src']
        nom = h3.text
        #print(compt+1, '\n', 'nom=',nom,'\n', 'url =', url, '\n','image =', image, '\n' )
        compt+=1
    # -------------------Recuperation des services --------------------------
        md5 = html_soup.findAll('div', attrs={'class': 'col-md-5'})
        services = []
        for itm in md5:
          titre = item.find('h3').text
          print(titre)
        

      
else:
  print(response.status_code)  


################ telechargement de video ##############
  apivideo : "https://downloader.freemake.com/api/videoinfo/8Hu8L7psTHQ"
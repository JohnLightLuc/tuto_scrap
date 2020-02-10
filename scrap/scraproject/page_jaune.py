import requests
from bs4 import BeautifulSoup
import json

url = "https://www.lespagesjaunesafrique.com/"
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    html_soup = BeautifulSoup(response.text, 'html.parser')
    sm12 = html_soup.findAll('div', attrs={'class': 'col-sm-12'})
    sm_pays = sm12[1]
    pays = []
    for item in sm_pays:
        dic = {}
        dic['pays'] =item.text
        a = item.find('a')
        dic['url'] = a['href']
        
        pays.append(dic)

    print(pays)
    
else:
    print(response.status_code)

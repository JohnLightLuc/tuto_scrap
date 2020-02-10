import requests
from bs4 import BeautifulSoup

url = "https://pratik.ci/thematiques/loisirs/confiserie"
response = requests.get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup)
entreprise = html_soup.find('div', attrs={'class': 'views-rows'})
print(entreprise)

# element = entreprise.find('div', attrs={'class': 'rows'}).get_text()
# telephone = element.find('div', attrs={'class': 'field field-name-field-telepone-1'})[2].get_text()
# print(telephone)
# cel = element.find('div', attrs={'class': 'field field-name-field-cellulaire1'}).get_text()
# print(cel)

tel = entreprise.find('div', attrs={'class': 'field-name-field-telepone-1'})
print(tel)
cel = entreprise.find('div', attrs={'class': 'field-name-field-cellulaire1'})
print(cel)
add = entreprise.find('div', attrs={'class': 'field-name-field-localisation-lieu'})
print(add)

siege = entreprise.find('div', attrs={'class': 'field-name-field-localisation-lieu'})



siege = entreprise.find('div', attrs={'class': 'field-name-field-siege'})

data = {
    'entreprise': entreprise,
    'tel': tel,
    'cel':cel,
    'add': add,
}


print(data)  
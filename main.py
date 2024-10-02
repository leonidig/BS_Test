import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Python_(programming_language)"


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


infobox = soup.find('table', {'class': 'infobox vevent'})


rows = infobox.find_all('tr')


data = {}


for row in rows:
    header = row.find('th')
    value = row.find('td')
    
    if header and value:
        key = header.text.strip()
        val = value.text.strip()
        data[key] = val


for key, val in data.items():
    print(f'{key}: {val}')

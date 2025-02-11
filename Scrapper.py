import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = 'https://www.mercadolibre.com.co/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_count = len(soup.find_all('h1'))
    h2_count = len(soup.find_all('h2'))
    h3_count = len(soup.find_all('h3'))

    print(f'Number of <h1> tags: {h1_count}')
    print(f'Number of <h2> tags: {h2_count}')
    print(f'Number of <h3> tags: {h3_count}')
else:
    print(f'Error accessing the page. Status code: {response.status_code}')

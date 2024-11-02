import re

import requests
from bs4 import BeautifulSoup

html_content = open('avans.html', 'r').read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all product containers
product_containers = soup.find_all('div', class_='c-offerBox_col is-last is-col4')

# Loop through each product container and extract URL and price
for container in product_containers:
    # Extract the URL
    url_tag = container.find('a', class_='is-installmentLink')
    url = 'https://www.avans.pl' + url_tag['href'] if url_tag else None
    if not url:
        continue
    model_id = re.findall(r'piekarnik-electrolux-([a-zA-Z0-9]{8,10})', url)
    # print(model_id)

    # Extract the price
    price_tag = container.find('div', class_='a-price_new')
    price = price_tag['data-price'] if price_tag else None

    print(f'ModelId: {model_id[0]} - Price: {int(price)/100} PLN - URL: {url} ')
from bs4 import BeautifulSoup
import requests
import sys
import time

url = "https://www.bike-discount.de/en/bike?o=14&n=100&p="
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
prod_urls = []
# for 2 pages of products
for i in range(1, 3):
    url = url + str(i)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    prod_divs = soup.find_all('div', {'class': "product--info"})
    for prod in prod_divs:
        prod_urls.append(prod.find('a')['href'])
    time.sleep(3)
print(*prod_urls, sep = '\n', file=sys.stdout)

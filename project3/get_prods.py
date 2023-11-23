from bs4 import BeautifulSoup
import csv
import requests
import sys
import time

# get initial values
filename = "urls.txt"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
if len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    lines_number = int(sys.argv[2])
else:
    lines_number = 0

file = open(filename, "r")
# restrict number of urls to process if second argument is provided
if lines_number != 0:
    file = [next(file) for _ in range(lines_number)]
    
# set up tsv writer    
writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')

for url in file:
    url = url.strip()
    frame_material = "unknown"
    wheel_size = "unknown"
    colour = "unknown"
    weight = "unknown"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # read product name and price
    prod_name = soup.find('h1', {'class': "product--title"}).text.strip()
    prod_price = soup.find('span', {'id': "netz-price"}).text.strip()
    # read specifications table
    spec_row = soup.find_all('tr', {'class': "product--properties-row"})
    for row in spec_row:
        vals = row.find_all('td')
        if vals:
            match vals[0].text:
                case "Frame material:":
                    frame_material = vals[1].text
                case "Wheel size:":
                    wheel_size = vals[1].text
                case "Colour:":
                    colour = vals[1].text
                case "Weight:":
                    weight = vals[1].text
                case _:
                    pass
    # write results to tsv
    writer.writerow([url, prod_name, prod_price, frame_material, wheel_size, colour, weight])
    # wait before next request
    time.sleep(3)

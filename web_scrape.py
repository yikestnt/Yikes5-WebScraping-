from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.safari.service import Service as SafariService

import requests
from bs4 import BeautifulSoup

#url = "https://www.vancleefarpels.com/us/en/collections/jewelry/alhambra/vcara45900---vintage-alhambra-pendant.html"
#url = 'https://news.ycombinator.com/item?id=29782099'

#url = 'https://laurieflemingjewellery.com/products/hidden-fairy-charm'
#url = 'https://www.cartier.com/en-us/jewelry/rings/love/love-ring-CRB4084600.html'
url = 'https://www.catbirdnyc.com/jewelry/collections/city-exclusive-charms.html'
#url = 'https://www.arkhamtechnology.com/solutions'
#url = 'https://www.reddit.com/user/BagUSeek/'

driver = webdriver.Safari()
    
driver.get(url)
    
# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
page_source = driver.page_source
#print(page_source)
    
driver.quit()

def main():
    
    #response = requests.get(url, headers= headers)
    
    #response = requests.get(url)
    

    elements = soup.find_all('li', class_="item product product-item")
    #print(elements)
    product_cards = soup.find_all('product-card')
    #print(product_cards)
    
    print(f"Elements Found: {len(elements)}")
    for i, element in enumerate(elements):
        print(f"Element {i + 1}:")
        #print("Raw HTML:")
        #print(element.prettify())  # Pretty-print HTML for better readability

        # Extract and print content inside the div
        div = element.find('div')
#         if div:
#             print("Div Content:")
#             print(div.prettify())
#         else:
#             print("No div found in this element.")
        
        # Extract and print specific details
        sold_out = product_cards[i].get('data-is-sold-out')
        print(sold_out)
        if (sold_out) == "1":
            print("it is sold out")
        name_tag = element.find('a', class_='product-item-link') # finds name of item 
        price_tag = element.find('span', class_='price')
        
        name = name_tag.text.strip() if name_tag else 'No name found'
        price = price_tag.text.strip() if price_tag else 'No price found'
        
        print(f"Product Name: {name}")
        print(f"Price: {price}")
        print('-' * 40)

    print(f"Scraping: {url}")
    
#collect based on inspecting the element of the webpage
#data-dimension10="In stock"

if __name__ == "__main__":
    main()

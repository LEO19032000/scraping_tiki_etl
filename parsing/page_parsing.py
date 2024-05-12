from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
# import pandas as pd
import logging

logger = logging.getLogger()

# constructor contains product data
class product_info:
    def __init__(self, category, price, title, discount,rating, total_sales, prod_id):
        self.category =category
        self.price = price
        self.title = title
        self.discount = discount
        self.total_sales = total_sales
        self.rating = rating
        self.prod_id = prod_id
# constructor contains links of each product
    def count(self):
        return len(self.prod_id)
        
class product_link:
    def __init__(self, image, product):
        self.image = image
        self.product = product
# got link extract from menu and number of page from main_build.py
def process_page(website_path,link, i):
    tuple_data = []
    tuple_data_page = []
    # request url: https://tiki.vn/nha-sach-tiki/c8322?page=2
    request_url = website_path +link+"?page="+i # 'https://tiki.vn/nha-sach-tiki/c8322&page=2'
    html = urlopen(request_url)
    # html paring
    bs = BeautifulSoup(html, 'html.parser')
    # list_prod_id = bs.find_all(attrs={"data-view-id": re.compile('.*')})
    list_prod_id = bs.find_all("div", attrs={"class":re.compile('CatalogProducts')})

    
    for prod in list_prod_id:
        # extracting data with pattern

        try:
            product_name = prod.find('h3').text.strip()
            price = prod.find(class_='price-discount__price').text.strip()

            discount_element = prod.find(class_='price-discount__discount')
            discount = discount_element.text.strip() if discount_element else 0

            image_url = prod.find('img')['srcset']
            # brand = prod.find('span', attrs={"class":re.compile('StyledItem')})['alt']
            rating = len(prod.find_all('g'))
            total_sales = prod.find('span', class_='quantity has-border').text.split()[-1]
            product_url = "https:" + prod.previous['href']
            data_review = prod.find("p", attrs={"class":"review"}).contents
            data_rating = prod.find("span", attrs={"style": re.compile('.*')})['style']
        except AttributeError:
            discount = 0
        except Exception:
            data_review = ['null']
            data_rating = 'null'
            
        #store and append into tuple object
        product_data = product_info(category=link,price=price,title=product_name,
                                 rating=rating, prod_id=hash(product_name), total_sales=total_sales, discount=discount,)

        # data_prod_link = prod.find("a", attrs={"data-id":re.compile('.*'), "href":re.compile('.*')})['href']
        # link_data = product_link(image=data_image_link,product=data_prod_link)
        
        tuple_data = tuple([
            product_data.prod_id,
            product_data.category,
            product_data.price,
            product_data.title,
            discount,
            product_data.rating,
            image_url,
            product_url,
            link+i
        ])
        tuple_data_page.append(tuple_data)
    return tuple_data_page

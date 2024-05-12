from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import logging

logger = logging.getLogger()

all_list = []

def menu_extract(link):
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    # extract a list of category
    menu_list = bs.find_all("div", attrs={"class":re.compile('StyledItemV2')})
    # menu_list = bs.find_all('div', class_='StyledItemV2')

    for menu in menu_list:
        # print(menu.title)
        # menu.next()

        menu_item = menu.find_all('a', href= True)
        all_list.append(menu_item[0]['href'])
    return all_list
# print on when a build done successfully
logger.info("Starting to crawl...")



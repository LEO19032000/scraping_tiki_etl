from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import logging

# Set up the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def menu_extract(link):
    try:
        # Fetch and parse the HTML
        html = urlopen(link)
        bs = BeautifulSoup(html, 'html.parser')

        # Find all sections with the class "StyledListItem"
        menu_sections = bs.find_all('div', class_=re.compile('StyledListItem'))

        # Initialize an empty list to store the links
        menu_list = []

        # Loop through each section to find the one containing "Danh mục"
        for section in menu_sections:
            # Find the title div within the section
            title_div = section.find('div', class_=re.compile('StyledTitle'))

            # Check if the title div contains the exact text "Danh mục"
            if title_div and title_div.get_text(strip=True) == "Danh mục":
                
                # Find all links within this "Danh mục" section
                menu_items = section.find_all('a', href=True)

                # Loop through each menu item and collect the href links
                for item in menu_items:
                    href = item.get('href')
                    title = item.get('title', 'No Title')

                    # Add the href link to the list
                    if href:
                        menu_list.append(href)

                # Once "Danh mục" is found, no need to check other sections
                break

        if not menu_list:
            logger.info("No menu items found under")

        return menu_list
        

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return []

logger.info("Scrawling data...")

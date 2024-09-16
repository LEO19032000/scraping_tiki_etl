from parsing.menu_parsing import menu_extract
from parsing.page_parsing import process_page
from utils.tikidb_config import ConfigParser, read_db_config
from utils.tikiparse_config import get_config
from database.insert_tikidb import insert_data

import logging
# import pandas as pd

logger = logging.getLogger()

parsing_config = get_config()
website_path = parsing_config.get('website_path', None) # https://tiki.vn/

all_category = menu_extract(website_path)

for link in all_category:
    category_link = link.split('/')[1]
    # all_data = []
    # columns_df = tuple(['id','category','price','title','rating','image_link','product_link','from_page_link'])
    # all_data.append(columns_df)
    for pageID in range(1, parsing_config.get('page_number') + 1, 1):
        
        logger.info("Processing page: %s, category: %s", pageID, category_link)
        data_df = (process_page( website_path,link, str(pageID)))

        for data in data_df:
            insert_data(data) 
    
    logger.info("Inserted data category: %s", category_link)
    break
   
logger.info("Crawling data done")

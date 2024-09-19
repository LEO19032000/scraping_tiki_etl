from parsing.menu_parsing import menu_extract
from parsing.page_parsing import process_page
from parsing.tikidb_config import ConfigParser, read_db_config
from parsing.tikiparse_config import get_config
from database.db_insert import insert_data
from database.db_connect import connect_db
from database.db_init import db_init
import logging
# import pandas as pd

logger = logging.getLogger()

parsing_config = get_config()
website_path = parsing_config.get('website_path', None)

all_category = menu_extract(website_path)
 
# check connection
connect_db()
# Call db_init to ensure the table exists before inserting data
db_init()

for link in all_category:

    category_link = link.split('/')[1]

    for pageID in range(1, parsing_config.get('page_number') + 1, 1):

        logger.info("Processing page: %s, category: %s", pageID, category_link)
        data_df = (process_page( website_path,link, str(pageID)))

        for data in data_df:
            insert_data(data) 
    
    logger.info("Inserted data category: %s", category_link)
       
logger.info("Crawling data done")

# from menu_parsing import menu_extract
# from page_parsing import process_page
# from tikiparse_config import ConfigObject, get_config
# from insert_tikidb import insert_data

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

# datetime service level messages
# Spunk: query data, level = Debug

all_category = menu_extract(website_path)

for link in all_category:
    all_data = []
    columns_df = tuple(['id','category','price','title','rating','image_link','product_link','from_page_link'])
    # all_data.append(columns_df)
    for pageID in range(2, parsing_config.get('page_number'), 1):
        logger.info("processing page: %s", pageID)
        data_df = (process_page( website_path,link, str(pageID)))
        for data in data_df:
            insert_data(data)
            logger.info("inserting data: %s", data)
    category_link = link.split('/')[2]
    logger.info("processing category %s:", category_link)
    # MUST change to your local folder
    # pd.DataFrame(all_data).to_csv(
    #     parsing_config.get('save_path')+category_link+".csv",
    #     encoding=parsing_config.get('dataframe')['encoding'],
    #     header=parsing_config.get('dataframe')['header'],
    #     index=parsing_config.get('dataframe')['index'])
logger.info("Crawling data done")

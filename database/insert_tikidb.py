# from tikidb_config import read_db_config
from utils.tikidb_config import read_db_config
import mysql.connector


import sys

"""
CREATE TABLE products (
    id FLOAT,
    category VARCHAR(255),
    price VARCHAR(50),
    title VARCHAR(255),
	discount VARCHAR(255),
    rating FLOAT,
    image_link VARCHAR(2000),
    product_link VARCHAR(2000),
    from_page_link VARCHAR(2000)
);
"""

def insert_data(data):
	query = "INSERT INTO products(id,category,price,title,discount,rating,image_link,product_link,from_page_link)"\
		"VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	args = [str(item) for item in data]
	try:
		db_config = read_db_config()
		conn = mysql.connector.connect(**db_config)
		cursor = conn.cursor()
		cursor.execute(query, args)
		conn.commit()
	except Exception as error:
		print(error)
		print(db_config)
		sys.exit(1)
	finally:
		cursor.close()
		conn.close()



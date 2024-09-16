from utils.tikidb_config import read_db_config
from database.init_db import db_init
import mysql.connector
import sys
  
def insert_data(data):

	# Call db_init to ensure the table exists before inserting data
	db_init()
	
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

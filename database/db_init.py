from parsing.tikidb_config import read_db_config
import mysql.connector
from mysql.connector import Error

# db_execute = 'create database tiki_scrapper_db'
table_execute = 'create table products (\
		id VARCHAR(255),\
		category TEXT(255),\
		price VARCHAR(255),\
		title VARCHAR(255),\
		discount VARCHAR(10),\
		rating VARCHAR(255),\
		image_link TEXT(255),\
		product_link TEXT(255),\
		from_page_link TEXT(255))'

def db_init():
	conn = None
	try:
		db_config = read_db_config()
		conn = mysql.connector.connect(**db_config)
		if conn.is_connected():
			print('connected to mysql database')
			cursor = conn.cursor()
			cursor.execute(table_execute)
			print('created table')
			
	except Error as e:
		print(e)
	finally:
		if conn is not None and conn.is_connected():
			conn.close()
			cursor.close()

if __name__ == '__main__':
	db_init()

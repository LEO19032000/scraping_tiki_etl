from mysql.connector import MySQLConnection, Error
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parsing.tikidb_config import read_db_config

def connect_db():
	db_config = read_db_config()
	
	conn = None
	try:
		print('connecting to mysql database...')
		conn = MySQLConnection(**db_config)
		if conn.is_connected():
			print('connection established')
		else:
			print('connection failed')
	except Error as error:
		print(error)
	finally:
		if conn is not None and conn.is_connected():
			conn.close()
			print('connection closed')



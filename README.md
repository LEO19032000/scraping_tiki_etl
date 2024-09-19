# Description

This ETL pipeline demonstrates how to scrape product data from the Tiki.vn website and store it in a MySQL database. The project extracts categories from the front-end, parses product details for each category, and saves the raw data for analysis.

## Workflow Steps

- Extract Categories: Start by extracting categories from the menu, resulting in a list of URLs (subcategories).
- Page Parsing: Use each URL as a parameter for page parsing to extract data from each product over a set number of pages (configurable).
- Store Data: Insert the raw extracted data into the MySQL database.

## Technique

- Python3
- Lib: BeautifulSoup, urllib, pandas, pyyml, requests 
`pip3 install requirements.txt`
- Install virtual environment
- Database: Mysql
  - I'm using a Docker container

## Start the Pipeline

- Start the Python venv
- Start the `main.py` file, run main_buid.py in visual studio code or shell 
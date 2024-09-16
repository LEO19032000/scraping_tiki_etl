<<<<<<< HEAD
# Description

This ETL pipeline example demonstrates how to extract data from the front-end and store it in a MySQL database.

## Technique

- Python3
- Lib: BeautifulSoup, urllib, pandas, pyyml, requests 
`pip3 install library.txt`

- Install virtual environment

```shell
  python -m venv demo
```

- Database: Mysql
  - I using a Docker container 

```shell
  docker pull mysql
  docker run --name mysql_container -e MYSQL_ROOT_PASSWORD="123456" -d mysql
```

## Workflow Steps

- Extract Categories: Start by extracting categories from the menu, resulting in a list of URLs (subcategories).
- Page Parsing: Use each URL as a parameter for page parsing to extract data from each product over a set number of pages (configurable).
- Store Data: Insert the raw extracted data into the MySQL database.

## Start the Pipeline

- Start the Python venv `(demo)`

```shell
demo\Scripts\Activate

```

- Start the `main_build.py` file, run main_buid.py in visual studio code or shell 

```shell
python3 main_build.py
```
=======
# Tiki_scrapper_pipeline
This ETL pipeline example demonstrates how to extract data from the front-end and store it in a MySQL database.
>>>>>>> 97bad75 (Initial commit)

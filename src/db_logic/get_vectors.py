import mysql.connector
import numpy as np
import json
import ast
from config.config import CONNECTION_CONFIG

def parse_float_list(string):
    try:
        return ast.literal_eval(string)
    except Exception as e:
        return f"Error parsing string: {e}"

def fetch_all_vectors():
    connection = mysql.connector.connect(**CONNECTION_CONFIG)
    cursor = connection.cursor()

    query = "SELECT vector_data FROM initiatives WHERE vector_data IS NOT NULL"
    cursor.execute(query)
    
    vector_list = []
    
    for (vector_data,) in cursor.fetchall():
        vector = parse_float_list(vector_data)
        vector_list.append(vector)

    cursor.close()
    connection.close()

    return vector_list

def fetch_all_titles():
    connection = mysql.connector.connect(**CONNECTION_CONFIG)
    cursor = connection.cursor()

    query = "SELECT title FROM initiatives WHERE vector_data IS NOT NULL"
    cursor.execute(query)
    
    title_list = []
    
    for (title_data,) in cursor.fetchall():
        title = title_data
        title_list.append(title)

    cursor.close()
    connection.close()

    return title_list

def fetch_all_urls():
    connection = mysql.connector.connect(**CONNECTION_CONFIG)
    cursor = connection.cursor()

    query = "SELECT initiative_url FROM initiatives WHERE vector_data IS NOT NULL"
    cursor.execute(query)
    
    url_list = []
    
    for (url_data,) in cursor.fetchall():
        url = url_data
        url_list.append(url)

    cursor.close()
    connection.close()

    return url_list
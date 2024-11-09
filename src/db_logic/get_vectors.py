import mysql.connector
import numpy as np
import json
import ast
# from config.config import CONNECTION_CONFIG

CONNECTION_CONFIG = {
    'host': "34.67.133.83",
    'user': "root",
    'port': "3308",
    'password': "pass",
    'database': "alrdmc"
}

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
    
    for (vector_data,) in cursor.fetchall:
        print(vector_data)
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


def fetch_all_columns():
    connection = mysql.connector.connect(**CONNECTION_CONFIG)
    cursor = connection.cursor()

    query = "SELECT * FROM initiatives"
    cursor.execute(query)
    
    result_list = []

    rows = cursor.fetchall()
    for row in rows:
        row_data = {}
        vector_data = None 
        
        for idx, column in enumerate(row):
            column_name = cursor.description[idx][0]
            
            if column_name == "vector_data" and column is not None and column != "":
                try:
                    vector_data = ast.literal_eval(column)
                except (ValueError, SyntaxError):
                    print(f"Error parsing vector_data for row: {row}")
                    vector_data = None 

            # Include the column in the dictionary even if it is empty or None
            row_data[column_name] = column
        
        if vector_data is not None:
            row_data["vector_data"] = vector_data  

        if row_data: 
            result_list.append(row_data)

    cursor.close()
    connection.close()

    return result_list


res = fetch_all_columns()

print(type(res))   # list, len = rows amount
print(len(res))

print(type(res[0]))  # of dictionaries
print(len(res[0]))


first_row = res[0]
title = first_row['title']

print(title)
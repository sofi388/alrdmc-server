import mysql.connector
import numpy as np
import json

# Database connection configuration
connection_config = {
    'host': "34.67.133.83",
    'user': "root",
    'port': "3308",
    'password': "pass",
    'database': "alrdmc"
}

# Connect to the database and fetch all vector data
def fetch_all_vectors():
    # Establish the connection
    connection = mysql.connector.connect(**connection_config)
    cursor = connection.cursor()

    # SQL query to fetch all non-null vectors
    query = "SELECT vector_data FROM initiatives WHERE vector_data IS NOT NULL"
    cursor.execute(query)
    
    # Initialize list to hold vectors
    vector_list = []
    
    for (vector_data,) in cursor.fetchall():
        # Convert from JSON (or adjust if stored differently) to numpy array
        vector = json.dumps(vector_data)
        vector_list.append(vector)

    # Close database connection
    cursor.close()
    connection.close()

    return vector_list





def fetch_all_titles():
    # Establish the connection
    connection = mysql.connector.connect(**connection_config)
    cursor = connection.cursor()

    # SQL query to fetch all non-null vectors
    query = "SELECT title FROM initiatives WHERE vector_data IS NOT NULL"
    cursor.execute(query)
    
    # Initialize list to hold vectors
    title_list = []
    
    for (title_data,) in cursor.fetchall():
        # Convert from JSON (or adjust if stored differently) to numpy array
        title = title_data
        title_list.append(title)

    # Close database connection
    cursor.close()
    connection.close()

    return title_list




def fetch_all_urls():
    # Establish the connection
    connection = mysql.connector.connect(**connection_config)
    cursor = connection.cursor()

    # SQL query to fetch all non-null vectors
    query = "SELECT initiative_url FROM initiatives WHERE vector_data IS NOT NULL"
    cursor.execute(query)
    
    # Initialize list to hold vectors
    url_list = []
    
    for (url_data,) in cursor.fetchall():
        # Convert from JSON (or adjust if stored differently) to numpy array
        url = url_data
        url_list.append(url)

    # Close database connection
    cursor.close()
    connection.close()

    return url_list





# Retrieve all vectors
semantic_vector_list = fetch_all_vectors()
title_list = fetch_all_titles()
url_list = fetch_all_urls()

print(type(semantic_vector_list[0]))
print(type(title_list[0]))
print(type(url_list[0]))

# Display results
# print("All vectors retrieved from the initiative table.")
# print(semantic_vector_list)

# print("All titles retrieved from the initiative table.")
# print(title_list)

# print("All urls retrieved from the initiative table.")
# print(url_list)

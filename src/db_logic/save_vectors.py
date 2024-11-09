import mysql.connector
import numpy as np
import json
from generate_semantic_vector import generate_semantic_vector


def save_to_mysql(text: str, vector: list):
    """
    Saves the text and semantic vector to MySQL database
    """
    connection = mysql.connector.connect(
        host="34.70.118.142",
        user="root",
        port="3308",
        password="pass",
        database="alrdmc"
    )

    cursor = connection.cursor()

    vector_json = json.dumps(vector)    
    query = "INSERT INTO semantic_vectors_test (vector_text, vector_data) VALUES (%s, %s)"
    cursor.execute(query, (text, vector_json))
    
    connection.commit()
    cursor.close()
    connection.close()
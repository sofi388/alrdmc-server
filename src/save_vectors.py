import mysql.connector
import numpy as np
import json
from semanticize import generate_semantic_vector


def save_vectors_to_db(vector: list):
    """
    Saves the text and semantic vector to MySQL database, test function
    """
    connection = mysql.connector.connect(
        host="34.70.118.142",
        user="root",
        port="3308",
        password="pass",
        database="alrdmc"
    )
    
    cursor = connection.cursor()

    # Convert the vector to a JSON string or BLOB. Don't know how to VECTOR
    vector_json = json.dumps(vector)
    
    query = "INSERT INTO initiatives (vector_data) VALUES (%s)"
    cursor.execute(query, (vector_json))
    
    connection.commit()
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Generate the semantic vector for the input text
    text = "Hello, how are you?"
    vector = generate_semantic_vector(text)
    
    vector_list = vector.tolist()

    # Save the text and vector to MySQL
    save_vectors_to_db(text, vector_list)
    print("Data saved to MySQL.")

import transformers
import requests
import mysql
import xml.etree.ElementTree as ET
from db_logic.semanticize import generate_semantic_vector
import json


# There's an RSS feed at https://www.otakantaa.fi/fi/rss/. We can use this to get the latest initiatives.

def fetch_otakantaa():
    response = requests.get("https://www.otakantaa.fi/fi/rss/")
    # This is XML - we can use the `xml` module to parse it.
    root = ET.fromstring(response.text)

    # Convert the XML to a list of dictionaries.
    return_data = []
    for item in root.findall("./channel/item"):
        return_data.append({
            "title": item.find("title").text,
            "url": item.find("link").text,
            "description": item.find("description").text,
        })

    return_data = return_data[:5]

    # The text is in finnish - we can use the `transformers` module to translate it to english.
    translator = transformers.pipeline("translation", model="Helsinki-NLP/opus-mt-fi-en")
    for item in return_data:
        item["title_en"] = translator(item["title"])[0]["translation_text"]
        item["description_en"] = translator(item["description"])[0]["translation_text"]
    
    connection = mysql.connector.connect(
        host="34.67.133.83",
        user="root",
        port="3308",
        password="pass",
        database="alrdmc"
    )
    
    # Get the semantic vectors for each title
    for item in return_data:
        generate_vector_from = item["title_en"] + "\n" + item["description_en"]
        item["vector"] = json.dumps(generate_semantic_vector(generate_vector_from))
    
    cursor = connection.cursor()
    
    query = "INSERT INTO initiatives (title, initiative_url, vector_data, description) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE vector_data=VALUES(vector_data)"

    for item in return_data:
        cursor.execute(query, (item["title_en"], item["url"], item["vector"], item["description_en"]))

    return return_data

if __name__ == "__main__":
    print(fetch_otakantaa())
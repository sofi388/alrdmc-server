import transformers
import requests
import mysql
import xml.etree.ElementTree as ET
from db_logic.semanticize import generate_semantic_vector
import json


# There's an RSS feed at https://www.otakantaa.fi/fi/rss/. We can use this to get the latest initiatives.
def fetch_otakantaa():
    try:
        fetch_otakantaa_do_the_work()
    except Exception as e:
        print(f"Error fetching Otakantaa data: {e}")

def fetch_otakantaa_do_the_work():
    print("Fetching Otakantaa data")
    response = requests.get("https://www.otakantaa.fi/fi/rss/")
    # This is XML - we can use the `xml` module to parse it.
    root = ET.fromstring(response.text)

    # Convert the XML to a list of dictionaries.
    return_data = []
    for item in root.findall("./channel/item"):
        try:
            return_data.append({
                "title": item.find("title").text,
                "url": item.find("link").text,
                "description": item.find("description").text,
            })
        except:
            print(f"Error parsing item: {item}")

    # The text is in finnish - we can use the `transformers` module to translate it to english.
    translator = transformers.pipeline("translation", model="Helsinki-NLP/opus-mt-fi-en")
    for item in return_data:
        try:
            item["title_en"] = translator(item["title"])[0]["translation_text"]
            item["description_en"] = translator(item["description"])[0]["translation_text"]
        except:
            print(f"Error translating item: {item}")
    
    connection = mysql.connector.connect(
        host="34.67.133.83",
        user="root",
        port="3308",
        password="pass",
        database="alrdmc"
    )
    
    # Get the semantic vectors for each title
    for item in return_data:
        try:
            generate_vector_from = item["title_en"] + "\n" + item["description_en"]
            item["vector"] = json.dumps(generate_semantic_vector(generate_vector_from))
        except:
            print(f"Error generating vector for item: {item}")
    
    cursor = connection.cursor()
    
    query = "INSERT INTO initiatives (title, initiative_url, vector_data, description) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE vector_data=VALUES(vector_data)"

    for item in return_data:
        if "title_en" not in item:
            continue
        try:
            cursor.execute(query, (item["title_en"], item["url"], item["vector"], item["description_en"]))
        except:
            print(f"Error inserting item: {item}")

    return return_data
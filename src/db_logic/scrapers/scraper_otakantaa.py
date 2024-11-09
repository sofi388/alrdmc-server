import transformers
import requests
import xml.etree.ElementTree as ET
from db_logic.semanticize import generate_semantic_vector
import json
from pathlib import Path
import mysql

# There's an RSS feed at https://www.otakantaa.fi/fi/rss/. We can use this to get the latest initiatives.
def fetch_otakantaa():
    try:
        response = requests.get("https://www.otakantaa.fi/fi/rss/")
        return fetch_otakantaa_do_the_work(response.text)
    except Exception as e:
        print(f"Error fetching Otakantaa data: {e}. Retrying with local dump")
        # Use src/db_logic/scrapers/rss_dump.rss
        try:
            with open(Path(__file__).parent / "rss_dump.rss", 'r') as f:
                return fetch_otakantaa_do_the_work(f.read())
        except Exception as e:
            print(f"Error fetching Otakantaa data from local dump: {e}")
            return []

def fetch_otakantaa_do_the_work(response_text):
    print("Fetching Otakantaa data")
    # This is XML - we can use the `xml` module to parse it.
    root = ET.fromstring(response_text)

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
        print("Translating item...")
        try:
            item["title"] = translator(item["title"])[0]["translation_text"]
            item["description"] = translator(item["description"])[0]["translation_text"]
        except:
            print(f"Error translating item: {item}")
    
    return return_data

if __name__ == "__main__":
    print(fetch_otakantaa())
from scraper import scrape_all
from semanticize import generate_semantic_vector
import mysql.connector
import json
import logging
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")  
DB_PORT = os.getenv("DB_PORT")  


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_initiatives_to_db(titles, original_titles, urls, descriptions, original_descriptions, vectors):
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        port=DB_PASSWORD,
        password=DB_NAME,
        database=DB_PORT
    )
    
    cursor = connection.cursor()
    
    query = "INSERT INTO initiatives (title, original_title, initiative_url, description, original_description, vector_data) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE vector_data=VALUES(vector_data)"
    
    for title, original_title, url, description, original_description, vector in zip(titles, original_titles, urls, descriptions, original_descriptions, vectors):
        cursor.execute(query, (title, original_title, url, description, original_description, vector))
    
    connection.commit()
    cursor.close()
    connection.close()


def poller(logger):
    logger.info(f"polling for new initiatives")
    data = scrape_all(logger)

    titles = []
    original_titles = []
    urls = []
    vectors = []
    descriptions = []
    original_descriptions = []

    logger.info(f"starting to poll with {len(data)} initiatives")
    logger.info(f"data: {data}")
    for item in data:
        titles.append(item['title'])
        original_titles.append(item['originalTitle'])
        urls.append(item['url'])
        descriptions.append(item['description'])
        original_descriptions.append(item['originalDescription'])
        vectors.append(json.dumps(generate_semantic_vector(item['title'] + item['description'])))
    logger.info(f"got {len(data)} initiatives, pushing to db")
    save_initiatives_to_db(titles, original_titles, urls, descriptions, original_descriptions, vectors)
    logger.info(f"pushed {len(data)} initiatives to db")


if __name__ == "__main__":
    poller(logger)

import mysql.connector
import json
import logging
from scraper_change import fetch_change
from semanticize import generate_semantic_vector
import concurrent.futures
from config.config import CHANGE_URLS
from config.config import CONNECTION_CONFIG


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_initiatives_to_db(titles, original_titles, urls, descriptions, original_descriptions, vectors):
    """
    Saves titles, URLs, and semantic vectors to the database.
    """
    try:
        connection = CONNECTION_CONFIG
        cursor = connection.cursor()
        
        query = """
        INSERT INTO initiatives (title, original_title, initiative_url, description, original_description, vector_data)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE vector_data=VALUES(vector_data)
        """
        
        for title, original_title, url, description, original_description, vector in zip(
            titles, original_titles, urls, descriptions, original_descriptions, vectors
        ):
            cursor.execute(query, (title, original_title, url, description, original_description, vector))
        
        connection.commit()
        logger.info(f"Inserted {len(titles)} records into the database.")
        
    except mysql.connector.Error as db_err:
        logger.error(f"Database error: {db_err}")
    finally:
        cursor.close()
        connection.close()


def poller(logger):
    data = fetch_change(CHANGE_URLS) 

    titles, original_titles, urls, descriptions, original_descriptions, vectors = [], [], [], [], [], []

    for item in data:
        titles.append(item['title'])
        original_titles.append(item['originalTitle'])
        urls.append(item['url'])
        descriptions.append(item['description'])
        original_descriptions.append(item['originalDescription'])
        
        try:
            vectors.append(json.dumps(generate_semantic_vector(item['title'] + item['description'])))
        except Exception as vec_err:
            logger.error(f"Error generating vector for item '{item['title']}': {vec_err}")
            print(type(item['title']))
            vectors.append(None) 

    valid_data = [(t, ot, u, d, od, v) for t, ot, u, d, od, v in zip(
        titles, original_titles, urls, descriptions, original_descriptions, vectors
    ) if v is not None]
    
    if valid_data:
        titles, original_titles, urls, descriptions, original_descriptions, vectors = zip(*valid_data)
        save_initiatives_to_db(titles, original_titles, urls, descriptions, original_descriptions, vectors)
    else:
        logger.warning("No valid data to insert into the database.")


if __name__ == "__main__":
    poller(logger)

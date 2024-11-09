from db_logic.scraper import scrape_all
from db_logic.semanticize import generate_semantic_vector
import mysql.connector
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_initiatives_to_db(titles, urls, descriptions, vectors):
    """
    Saves title, initiative url and semantic vector of the title.
    """
    connection = mysql.connector.connect(
        host="34.67.133.83",
        user="root",
        port="3308",
        password="pass",
        database="alrdmc"
    )
    
    cursor = connection.cursor()
    
    query = "INSERT INTO initiatives (title, initiative_url, description, vector_data) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE vector_data=VALUES(vector_data)"
    
    for title, url, description,vector in zip(titles, urls, descriptions, vectors):
        cursor.execute(query, (title, url, description, vector))
    
    connection.commit()
    cursor.close()
    connection.close()


def poller(logger):
    logger.info(f"polling for new initiatives")
    data = scrape_all(logger)

    titles = []
    urls = []
    vectors = []
    descriptions = []

    logger.info(f"starting to poll with {len(data)} initiatives")
    logger.info(f"data: {data}")
    for item in data:
        titles.append(item['title'])
        urls.append(item['url'])
        descriptions.append(item['description'])
        vectors.append(json.dumps(generate_semantic_vector(item['title'] + item['description'])))
    logger.info(f"got {len(data)} initiatives, pushing to db")
    save_initiatives_to_db(titles, urls, descriptions, vectors)
    logger.info(f"pushed {len(data)} initiatives to db")




if __name__ == "__main__":
    poller(logger)

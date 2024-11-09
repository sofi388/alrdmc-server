# from config.config import POLLING_INTERVAL
from db_logic.scraper import scrape_all
from db_logic.semanticize import generate_semantic_vector
from db_logic.scraper_objectives import fetch_objective_from_url
import mysql.connector
import json
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def save_initiatives_to_db(titles, urls, vectors):#, objectives):
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
    
    query = "INSERT INTO initiatives (title, initiative_url, vector_data) VALUES (%s, %s, %s)"
    
    for title, url, vector in zip(titles, urls, vectors):
        cursor.execute(query, (title, url, vector))

    # for title, url, vector, objective in zip(titles, urls, vectors, objectives):
    #     cursor.execute(query, (title, url, vector, objective))
    
    connection.commit()
    cursor.close()
    connection.close()


def poller(logger):
    data = scrape_all()

    titles = []
    urls = []
    vectors = []
    objectives = []

    logger.info(f"starting to poll")
    for item in data:
        titles.append(item['title'])
        urls.append(item['url'])
        vectors.append(json.dumps(generate_semantic_vector(item['title'])))
        # objectives.append(fetch_objective_from_url(item['url']))

    save_initiatives_to_db(titles, urls, vectors) #, objectives)

    logger.info(f"got {len(data)} initiatives, pushing to db")



if __name__ == "__main__":
    poller(logger)

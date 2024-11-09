import requests
from config.config import EU_URL, KANSALAISALOITE_URL

from db_logic.scrapers.scraper_europe_initiatives import fetch_european_initiatives
from db_logic.scrapers.scraper_kansalaisaloite import fetch_kansalaisaloite
from db_logic.scrapers.scraper_otakantaa import fetch_otakantaa

def scrape_all(logger):
    data = []
    logger.info(f"fetch otakanta")
    try:
        data += fetch_otakantaa()
    except Exception as e:
        logger.error(f"Error fetching otakantaa data: {e}")
    logger.info(f"fetch kansalaisaloite, data={data}")
    try:
        data += fetch_kansalaisaloite()
    except Exception as e:
        logger.error(f"Error fetching kansalaisaloite data: {e}")

    logger.info(f"fetch european initiatives, data={data}")
    try:
        data += fetch_european_initiatives()
    except Exception as e:
        logger.error(f"Error fetching european initiatives data: {e}")
    logger.info(f"finished scraping, data={data}")

    return data


import requests
from config.config import EU_URL, KANSALAISALOITE_URL

from db_logic.scrapers.scraper_europe_initiatives import fetch_european_initiatives
from db_logic.scrapers.scraper_kansalaisaloite import fetch_kansalaisaloite
from db_logic.scrapers.scraper_otakantaa import fetch_otakantaa

def scrape_all(logger):
    logger.info(f"fetch otakanta")
    data = fetch_otakantaa()
    logger.info(f"fetch kansalaisaloite")
    data += fetch_kansalaisaloite()
    logger.info(f"fetch european initiatives")
    data += fetch_european_initiatives()
    return data

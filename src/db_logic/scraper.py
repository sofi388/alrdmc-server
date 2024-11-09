import requests
from config.config import EU_URL, KANSALAISALOITE_URL

from db_logic.scrapers.scraper_europe_initiatives import fetch_european_initiatives
from db_logic.scrapers.scraper_kansalaisaloite import fetch_kansalaisaloite
from db_logic.scrapers.scraper_otakantaa import fetch_otakantaa
from db_logic.scrapers.scraper_change import fetch_initiative_change
import concurrent.futures

def scrape_all(logger):
    scrapers = []
    data = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(scraper): scraper.__name__ for scraper in scrapers}
        for future in concurrent.futures.as_completed(futures):
            scraper_name = futures[future]
            try:
                data += future.result()
            except Exception as e:
                logger.error(f"Error fetching {scraper_name} data: {e}")
            logger.info(f"finished scraping {scraper_name}, data={data}")

    return data


import requests
# from config.config import EU_URL, KANSALAISALOITE_URL

<<<<<<< HEAD
EU_URL = "https://register.eci.ec.europa.eu/core/api/register/search/ALL/EN/0/20"
KANSALAISALOITE_URL = "https://www.kansalaisaloite.fi/fi/hae?searchView=pub&offset=0&limit=500&orderBy=mostTimeLeft&show=running"

#from scrapers.scraper_europe_initiatives import fetch_european_initiatives
#from scrapers.scraper_kansalaisaloite import fetch_kansalaisaloite
#from scrapers.scraper_otakantaa import fetch_otakantaa
from scrapers.scraper_change import fetch_change
import concurrent.futures

def scrape_all(logger):
    scrapers = [fetch_change] #fetch_otakantaa, fetch_kansalaisaloite, fetch_european_initiatives, fetch_change]
=======
from db_logic.scrapers.scraper_europe_initiatives import fetch_european_initiatives
from db_logic.scrapers.scraper_kansalaisaloite import fetch_kansalaisaloite
from db_logic.scrapers.scraper_otakantaa import fetch_otakantaa
from db_logic.scrapers.scraper_change import fetch_initiative_change
import concurrent.futures

def scrape_all(logger):
    scrapers = [fetch_european_initiatives, fetch_otakantaa, fetch_initiative_change]
>>>>>>> cf70a5609722d2b23116f095dd8dec7a985b9535
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


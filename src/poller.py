from config.config import POLLING_INTERVAL
from scraper import scrape_all

def periodic_poller(logger):
    while True:
        logger.info(f"polling for new initiatives after {POLLING_INTERVAL} seconds")
        time.sleep(POLLING_INTERVAL)
        logger.info(f"scraping initiatives")
        data = scrape_all()
        logger.info(f"got {len(data)} initiatives, pushing to db")
        # push to db
        
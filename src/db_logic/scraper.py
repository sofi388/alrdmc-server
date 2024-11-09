import requests
from config.config import EU_URL, KANSALAISALOITE_URL

from db_logic.scrapers.scraper_europe_initiatives import fetch_european_initiatives
from db_logic.scrapers.scraper_kansalaisaloite import fetch_kansalaisaloite

def scrape_all():
    data = []
    data += fetch_kansalaisaloite()
    data += fetch_european_initiatives()
    return data

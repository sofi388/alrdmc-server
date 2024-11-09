import requests
from config.config import EU_URL, KANSALAISALOITE_URL
from db_logic.scraper_objectives import fetch_objective_from_url

def fetch_kansalaisaloite():
    return []

def fetch_european_initiatives():
    objectives = fetch_objective_from_url(EU_URL)
    response = requests.get(EU_URL)
    response_dict = response.json()['entries']

    return_data = []

    for initiative in response_dict:
        if "title" not in initiative or "supportLink" not in initiative:
            continue

        initiative_object = {
            "title": initiative["title"],
            "url": f"https://citizens-initiative.europa.eu/initiatives/details/{initiative['year']}/{initiative['number']}",
        }

        return_data.append(initiative_object)

    return return_data

def scrape_all():
    data = []
    data += fetch_kansalaisaloite()
    data += fetch_european_initiatives()
    return data

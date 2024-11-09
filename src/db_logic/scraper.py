import requests
# from config.config import EU_URL, KANSALAISALOITE_URL

EU_URL =  "https://register.eci.ec.europa.eu/core/api/register/search/ALL/EN/0/20"

def fetch_kansalaisaloite():
    return []

def fetch_european_initiatives():
    response = requests.get(EU_URL)
    response_dict = response.json()['entries']

    return_data = []

    for initiative in response_dict:
        if "title" not in initiative or "supportLink" not in initiative:
            continue

        initiative_object = {
            "title": initiative["title"],
            "url": initiative["supportLink"],
        }

        return_data.append(initiative_object)

    return return_data

def scrape_all():
    data = []
    data += fetch_kansalaisaloite()
    data += fetch_european_initiatives()
    return data

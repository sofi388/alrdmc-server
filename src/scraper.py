import requests

url = "https://register.eci.ec.europa.eu/core/api/register/search/ALL/EN/0/20"

def fetch_european_initiatives(url: str):
    response = requests.get(url)
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
    

if __name__ == "__main__":
    data = fetch_european_initiatives(url)
    print(data)
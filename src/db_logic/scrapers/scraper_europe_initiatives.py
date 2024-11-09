from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import GOOGLE_DRIVER_LOC

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
            "description": fetch_objective_from_url(initiative["supportLink"])
        }

        return_data.append(initiative_object)

    return return_data

def fetch_objective_from_url(url: str):
    options = webdriver.ChromeOptions()
    options.binary_location = GOOGLE_DRIVER_LOC
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    
    try:
        objective_div = driver.find_element(By.ID, "initiativeDetails")
        objective_text = objective_div.text.strip()
        
        if objective_text:
            return objective_text
        else:
            print("Objective text not found")
            return " "
    except Exception as e:
        print(f"Error extracting objective: {e}")
        return " "
    finally:
        driver.quit()
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from config.config import CHANGE_URLS


def fetch_initiative_change(url: str):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    
    initiatives = []

    try:
        objective_divs = driver.find_elements(By.CLASS_NAME, "corgi-1vlmmoi")

        for div in objective_divs:
            title = div.text.strip()

            parent = div.find_element(By.XPATH, "./ancestor::a")
            url = parent.get_attribute("href") if parent else None

            if title and url:
                initiatives.append({
                    "title": title,
                    "url": url,
                    "originalTitle": title
                })

        return initiatives

    except Exception as e:
        print(f"Error extracting initiatives: {e}")
        return []
    finally:
        driver.quit()


def fetch_descriptions_for_initiatives(initiatives: dict):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    try:
        for initiative in initiatives.values():
            driver.get(initiative["url"])
            time.sleep(1)  

            try:
                description_element = driver.find_element(By.CLASS_NAME, "e19irtt30.corgi-1qn3huw")
                description_text = description_element.text.strip()
                initiative["description"] = description_text
                initiative["originalDescription"] = description_text
            except Exception as e:
                print(f"Error fetching description from {initiative['url']}: {e}")
                initiative["description"] = "No description found"
                initiative["originalDescription"] = "No description found"

    finally:
        driver.quit()


def fetch_change(urls=CHANGE_URLS):
    res = []

    for url in urls:
        res += fetch_initiative_change(url)

    unique_initiatives = {initiative['url']: initiative for initiative in res}
    fetch_descriptions_for_initiatives(unique_initiatives)

    res = list(unique_initiatives.values())

    return res


if __name__ == "__main__":
    print(fetch_change())
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import GOOGLE_DRIVER_LOC, KANSALAISALOITE_URL

def fetch_kansalaisaloite():
    options = webdriver.ChromeOptions()
    options.binary_location = GOOGLE_DRIVER_LOC
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(KANSALAISALOITE_URL)
    driver.implicitly_wait(10)
    
    try:
        list_items = driver.find_elements(By.TAG_NAME, "li")
        list_contents = [
                    {
                        "title": item.text.strip(), 
                        "url": item.find_element(By.TAG_NAME, "a").get_attribute("href"),
                    }
                for item in list_items if item.text.strip()]

        if list_contents:
            return list_contents
        else:
            print("No list items found")
            return " "
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

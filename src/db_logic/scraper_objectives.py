from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def fetch_objective_from_url(url: str):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

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

def fetch_kansalaisaloite_lists_from_url(url: str):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    
    try:
        list_items = driver.find_elements(By.TAG_NAME, "li")
        list_contents = [item.text.strip() for item in list_items if item.text.strip()]
        
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

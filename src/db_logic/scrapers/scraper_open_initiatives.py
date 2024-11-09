import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def fetch_initiative_links_and_texts(url: str):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')  
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
        driver.get(url)
        driver.implicitly_wait(10)
        
        try:
            # Get all elements with the specified class
            objective_divs = driver.find_elements(By.CLASS_NAME, "op__link--inherited-style")
            
            # Extract text and link from each element
            initiatives = [
                {
                    "title": div.text.strip(),
                    "originalTitle": div.text.strip(),
                    "description": div.text.strip(), 
                    "originalDescription": div.text.strip(),
                    "url": div.get_attribute("href"),
                }
                for div in objective_divs if div.text.strip() and div.get_attribute("href")
            ]
            
            # Regular expression to match only Latin characters (letters, basic punctuation)
            latin_regex = re.compile(r'^[A-Za-z0-9\s\.,!?;:()"\'-]*$')
            
            # Filter only initiatives with Latin characters
            latin_initiatives = [
                initiative for initiative in initiatives 
                if latin_regex.match(initiative['text'])
            ]
            
            if latin_initiatives:
                return latin_initiatives
            else:
                print("No initiatives with Latin characters found")
                return []
        except Exception as e:
            print(f"Error extracting initiatives: {e}")
            return []


res = fetch_initiative_links_and_texts('https://www.openpetition.eu/petitionen')


print(res)
print(len(res))

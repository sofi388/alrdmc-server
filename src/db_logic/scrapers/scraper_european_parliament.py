import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

url = "https://www.europarl.europa.eu/petitions/en/show-petitions?keyWords=&years=2024&_years=1&_searchThemes=1&statuses=AVAILABLE&_statuses=1&_countries=1&searchRequest=true&resSize=10&pageSize=10#res"
# url = "https://www.europarl.europa.eu/petitions/en/show-petitions?keyWords=&years=2024&_years=1&_searchThemes=1&statuses=AVAILABLE&_statuses=1&_countries=1&searchRequest=true&resSize=100&pageSize=100#res"

def fetch_parliament(url=url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        driver.implicitly_wait(10)  # Wait for the page to load
        
        initiatives = []
        
        elements = driver.find_elements(By.CLASS_NAME, "petition_title")
        
        for i in range(0, len(elements), 2):
            title = elements[i].text.strip() 
            
            description = elements[i + 1].text.strip() if i + 1 < len(elements) else ""
            
            link_element = elements[i].find_element(By.XPATH, "./ancestor::h2/a")
            link = link_element.get_attribute("href")
            
            if title and link:
                initiatives.append({
                    "title": title,
                    "description": description,
                    "url": link,
                    "originalTitle": title,
                    "originalDescription": description

                })
                
        return initiatives

    except Exception as e:
        print(f"Error extracting initiatives: {e}")
        return []
    
    finally:
        driver.quit()


"""
Test results
"""
res = fetch_parliament(url)

for initiative in res:
    print(f"Title: {initiative['title']}")
    print(f"Description: {initiative['description']}")
    print(f"Link: {initiative['url']}")
    print()
print(f"Number of initiatives: {len(res)}")

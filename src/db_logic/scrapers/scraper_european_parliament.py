import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

urls = "https://www.europarl.europa.eu/petitions/en/show-petitions?keyWords=&years=2024&_years=1&_searchThemes=1&statuses=AVAILABLE&_statuses=1&_countries=1&searchRequest=true&resSize=100&pageSize=100#res"

def fetch_initiative_parliament(url: str):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Setup WebDriver service
    service = Service(ChromeDriverManager().install())

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        driver.implicitly_wait(10)  # Wait for the page to load
        
        initiatives = []
        
        # Find all petition links that are paired with titles and descriptions
        petition_links = driver.find_elements(By.CSS_SELECTOR, "a.t-item")
        
        for i in range(0, len(petition_links), 2):
            # Extract the title
            title_element = petition_links[i].find_element(By.CLASS_NAME, "petition_title")
            title = title_element.text.strip()
            
            # Extract URL for each petition
            url = petition_links[i].get_attribute("href")
            
            # Extract the description (usually follows the title)
            description_element = petition_links[i + 1].find_element(By.CLASS_NAME, "petition_title").text.strip() if i + 1 < len(petition_links) else ""
            
            if title and description_element and url:
                initiatives.append({
                    "title": title,
                    "description": description_element,
                    "url": url
                })
                
        return initiatives

    except Exception as e:
        print(f"Error extracting initiatives: {e}")
        return []
    
    finally:
        driver.quit()

# Fetch and print the results
res = fetch_initiative_parliament(urls)
for initiative in res:
    print(f"Title: {initiative['title']}")
    print(f"Description: {initiative['description']}")
    print(f"URL: {initiative['url']}")
    print()
print(f"Number of initiatives: {len(res)}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def fetch_objective_from_url(url: str):
    # Initialize the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.headless = True  # Optional: run in headless mode (without opening a browser window)
    
    # Use WebDriver Manager to automatically manage the ChromeDriver installation
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the URL
    driver.get(url)
    
    # Allow time for page to load and execute JavaScript (if necessary)
    driver.implicitly_wait(10)
    
    try:
        # Find the div containing the objectives
        objective_div = driver.find_element(By.ID, "initiativeDetails")
        
        # Extract the objective text
        objective_text = objective_div.text.strip()
        
        if objective_text:
            return objective_text
        else:
            print("Objective text not found")
            return None
    except Exception as e:
        print(f"Error extracting objective: {e}")
        return None
    finally:
        # Close the browser window
        driver.quit()

# Example of how to use the function:
url = "https://eci.ec.europa.eu/045/public/#/screen/home"
# url = "https://eci.ec.europa.eu/047/public/?lg=en"
objective_text = fetch_objective_from_url(url)

if objective_text:
    print("Objective Text Extracted:")
    print(objective_text)
else:
    print("No objective text available.")

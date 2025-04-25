from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def browser_automation_with_selenium():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Path to the ChromeDriver executable
    # Replace with the actual path to your ChromeDriver
    chrome_driver_path = "chromedriver"

    # Create a new Chrome browser instance
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the Google homepage
    driver.get("https://www.google.com")

    # Find the search box and enter a query
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    driver.implicitly_wait(5)

    # Print the title of the search results page
    print("Page title:", driver.title)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    browser_automation_with_selenium()

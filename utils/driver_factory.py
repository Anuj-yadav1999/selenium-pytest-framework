# Reusable webdriver setup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Run in headless mode
    options.add_argument("--start-maximized") # Start maximized
    options.add_arguments("--disable-gpu") # Disable GPU acceleration

    # Create a new instance of Chrome driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitely_wait(10) # Implicit wait for 10 seconds
    return driver

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure logging
def setup_logger(username):
    logger = logging.getLogger(username)
    logger.setLevel(logging.ERROR)
    log_file = f"{username}_log.log"
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

accepted_usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]

options = Options()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# Replace 'C:\\chromedriver\\chromedriver.exe' with the actual path of the Chromedriver executable
chrome_path = 'C:\\chromedriver\\chromedriver.exe'
service = Service(chrome_path)

for username in accepted_usernames:
    try:
        # Set up logger for the current user
        logger = setup_logger(username)

        # Use the Chrome service while initializing the WebDriver with options
        driver = webdriver.Chrome(service=service, options=options)

        # Navigate to the Swag Labs login page
        driver.get("https://www.saucedemo.com/")

        # Wait for the username field to be present
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))

        # Find the username and password fields and enter credentials
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys(username)
        password_field.send_keys("secret_sauce")

        # Click the login button
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Wait for a moment to let the page load properly
        time.sleep(2)

        # Add an item to the shopping cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Rest of the test script...

        # Close the browser and end the WebDriver session
        driver.quit()

    except Exception as e:
        # Log the error to the user-specific log file
        logger.exception("An error occurred during script execution:")
        # Close the browser and end the WebDriver session
        driver.quit()

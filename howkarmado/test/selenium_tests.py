from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys  

def test_can_we_host_some_locals():
    sauce_url = "http://dylanatsauce:65f828c5-8ef0-48a7-8d2d-f06d08150020@ondemand.saucelabs.com:80/wd/hub"

    desired_capabilities = {
        'platform': "Mac OS X 10.9",
        'browserName': "chrome",
        'version': "31",
    }

    driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                              command_executor=sauce_url)
    driver.implicitly_wait(10)
    driver.get("http://localhost:8000")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "summary"))
        )
    finally:
        driver.quit()
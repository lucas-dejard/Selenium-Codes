from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.yatra.com")
try:
    wait = WebDriverWait(driver, 40).until(ec.element_to_be_clickable((By.CLASS_NAME, 'btngdpr'))).click()

finally:
    driver.find_element(By.ID, 'BE_flight_flsearch_btn').click()

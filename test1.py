from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://www.yatra.com")

driver.find_element(By.ID, 'BE_flight_flsearch_btn').click()

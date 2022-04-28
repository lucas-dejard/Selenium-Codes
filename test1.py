from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class DemoDropDown():
    def demo_drop(self):
        driver.get("https://www.salesforce.com/br/form/signup/freetrial-sales-pe/")
        driver.select(By.ID, 'BE_flight_flsearch_btn').click()

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class DemoDropDown():
    def demo_drop(self):
        driver.get("https://www.salesforce.com/br/form/signup/freetrial-sales-pe/")
        dropdown = driver.find_element(By.NAME, 'CompanyEmployees')
        dd = Select(dropdown)
        dd.select_by_value('10')
        time.sleep(3)
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_visible_text('21 - 50 funcionários')
        time.sleep(3)
        driver.quit()

DemoDropDown().demo_drop()
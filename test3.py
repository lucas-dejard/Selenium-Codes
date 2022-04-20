from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class DemoDropDown():
    def demo_drop(self):
        driver.get("https://mdbootstrap.com/docs/standard/extended/multiselect/")
        dropdown = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div/div[1]/section/section[2]/'
                                                 'section[1]/div/section/div/div/select')
        dd = Select(dropdown)
        time.sleep(3)
        dd.select_by_value('1')
        time.sleep(3)
        driver.quit()

DemoDropDown().demo_drop()



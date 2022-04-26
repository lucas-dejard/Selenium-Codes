from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class DemoTest:
    def demo_sugest(self):
        driver.get("https://www.yatra.com/")
        dropdown = driver.find_element(By.ID, 'BE_flight_origin_city')
        dropdown.click()
        time.sleep(3)
        dropdown.send_keys("New Del")
        time.sleep(3)
        dropdown.send_keys(Keys.ENTER)
        time.sleep(3)

        dropdown2 = driver.find_element(By.ID, 'BE_flight_arrival_city')
        dropdown2.send_keys("New")
        dropdown3 = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(dropdown3))
        for i in dropdown3:
            print(i.text)
        driver.quit()


DemoTest().demo_sugest()

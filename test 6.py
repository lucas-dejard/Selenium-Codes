from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class DemoTest:
    def demo_calendar(self):
        driver.get("https://www.yatra.com/")
        calendar = driver.find_element(By.ID, 'BE_flight_origin_date')
        calendar.click()
        time.sleep(3)
        alldates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        calendar.click()
        for date in alldates:
            if date.get_attribute("data-date") == "20/05/2022":
                date.click()
                break
        time.sleep(3)

        driver.quit()


DemoTest().demo_calendar()

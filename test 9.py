from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class MultipleWindows:
    def multi_w(self):
        driver.get("https://www.yatra.com")
        banner = driver.find_element(By.XPATH,"//img[@class='conta iner']")
        banner.click()
        all_handle = driver.window_handles
        now_handle = driver.current_window_handle
        print(all_handle)
        print(now_handle)
        for handle in all_handle:
            if handle != now_handle:
                driver.switch_to.window(handle)
                time.sleep(5)
                banner2 = driver.find_element(By.ID, "BE_flight_flsearch_btn")
                banner2.click()
                time.sleep(2)
                driver.close()
                time.sleep(2)

MultipleWindows().multi_w()
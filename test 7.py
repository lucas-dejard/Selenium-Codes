from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class DemoTest:
    def demo_login(self):
        driver.get("https://secure.yatra.com/social/common/yatra/signin.html")
        log = driver.find_element(By.ID, 'login-continue-btn')
        log.screenshot(".\\test.png")
        log.click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\Intel\\error.jpg")
        time.sleep(3)
        driver.save_screenshot(".\\test1.png")

        driver.quit()


DemoTest().demo_login()

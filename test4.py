from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


class DemoDropDown():
    def demo_drop(self):
        driver.get("https://preview.colorlib.com/theme/bootstrap/multiselect-20/")
        driver.find_element(By.CLASS_NAME, 'chosen-choices').click()
        dropdown = driver.find_element(By.XPATH, "//div[@id='multiple_label_example_chosen']//"
                                                  "li[@class='active-result'][normalize-space()='HTML5']").click()

        time.sleep(3)
        driver.quit()


DemoDropDown().demo_drop()

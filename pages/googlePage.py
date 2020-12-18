
from selenium.webdriver.common.keys import Keys


class GooglePage():
    def __init__(self, driver):
        self.driver = driver

        self.search_box_id = "//input[@title='Поиск']"
        self.linkedin_link_id = "//span[contains(text(),'LinkedIn Россия: войти или зарегистрироваться')]"

    def enter_linkedin(self, linkedins):
        enter = self.driver.find_element_by_xpath(self.search_box_id)
        enter.clear()
        enter.send_keys(linkedins)
        enter.send_keys(Keys.ENTER)

    def click_linkedin_link(self):
        link = self.driver.find_element_by_xpath(self.linkedin_link_id)
        link.click()

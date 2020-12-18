from selenium.webdriver.common.keys import Keys


class LinkedinPage():
    def __init__(self, driver):
        self.driver = driver

        self.button_enter_id = "//a[contains(text(),'Войти')]"
        self.username_text_id = "//input[@id='login-email']"
        self.password_text_id = "//input[@id='login-password']"
        self.button_enter_link_id = "//input[@id='login-submit']"
        self.body_page = "body"
        self.search_box_id = "//input[@placeholder='Search']"
        self.job_button_id = "//button[normalize-space()='Jobs']"

    def enter_button(self):
        button1 = self.driver.find_element_by_xpath(self.button_enter_id)
        button1.click()

    def enter_username(self, username):
        login_name = self.driver.find_element_by_xpath(self.username_text_id)
        login_name.clear()
        login_name.send_keys(username)

    def enter_password(self, password):
        password1 = self.driver.find_element_by_xpath(self.password_text_id)
        password1.clear()
        password1.send_keys(password)

    def enter_button_link(self):
        button2 = self.driver.find_element_by_xpath(self.button_enter_link_id)
        button2.click()

    def enter_job(self, job):
        search = self.driver.find_element_by_xpath(self.search_box_id)
        search.clear()
        search.send_keys(job)
        search.send_keys(Keys.ENTER)

    def click_job_button(self):
        clickb = self.driver.find_element_by_xpath(self.job_button_id)
        clickb.click()




from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GlassdoorPage():

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_button = "//a[contains(text(),'Sign In')]"
        self.username_text_id = "//input[@id='userEmail']"
        self.password_text_id = "//input[@id='userPassword']"
        self.enter_button_id = "//button[normalize-space()='Sign In']"
        self.searching_job_text_id = "//input[@id='sc.keyword']"

    def sign_in(self):
        signinButton = self.driver.find_element(By.XPATH, self.sign_in_button)
        signinButton.click()

    def enter_login(self, username):
        glassdoorName = self.driver.find_element(By.XPATH, self.username_text_id)
        glassdoorName.clear()
        glassdoorName.send_keys(username)

    def enter_password(self, password):
        enterPassword = self.driver.find_element(By.XPATH, self.password_text_id)
        enterPassword.clear()
        enterPassword.send_keys(password)

    def enter_button(self):
        enterButton = self.driver.find_element(By.XPATH, self.enter_button_id)
        enterButton.click()

    def enter_job(self, job):
        enterJob = self.driver.find_element(By.XPATH, self.searching_job_text_id)
        enterJob.clear()
        enterJob.send_keys(job)
        enterJob.send_keys(Keys.ENTER)

import time
import moment
import allure
import pytest
from utils import utils as utils
from pages.googlePage import GooglePage
from pages.linkedinPage import LinkedinPage
from pages.glassdoorPage import GlassdoorPage


@pytest.mark.usefixtures("test_setup")
class TestGoogle():

    def test_man_search(self):
        try:
            driver = self.driver
            driver.get(utils.URL_FJ)
            x = driver.title
            assert x == "5 Tips for Locating Telecommute-Friendly Companies"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            screenshotName = "screenshot_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/baski/StepAcademy/screenshots" +screenshotName + ".png")
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("No exception occurred")
        finally:
            print("I am inside finally block")

    def test_search(self):
        driver = self.driver
        driver.get(utils.URL)

        search = GooglePage(driver)
        search.enter_linkedin(utils.LINKEDIN)
        search.click_linkedin_link()

    def test_linkedin(self):
        driver = self.driver
        linkpage = LinkedinPage(driver)
        linkpage.enter_button()
        linkpage.enter_username(utils.USERNAME)
        linkpage.enter_password(utils.PASSWORD)
        linkpage.enter_button_link()
        linkpage.enter_job(utils.JOB)
        linkpage.click_job_button()
        time.sleep(3)

    def test_glassdoor(self):

        driver = self.driver
        driver.get(utils.URL_G)
        glassdoorpage = GlassdoorPage(driver)
        glassdoorpage.sign_in()
        glassdoorpage.enter_login(utils.USERNAME1)
        glassdoorpage.enter_password(utils.PASSWORD1)
        glassdoorpage.enter_button()
        glassdoorpage.enter_job(utils.JOB)

    def test_picture(self):
        driver = self.driver
        driver.get(utils.URL_P)

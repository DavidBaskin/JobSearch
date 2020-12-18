from appium import webdriver
from selenium.webdriver.common.by import By

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "/path/to/the/downloaded/ApiDemos-debug.apk",

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

driver.implicitly_wait(5)

driver.find_element(By.ID, "fsgnsglksjglkse").click()

e = driver.find_element(By.ID, "sefsegfsef")
e.clear()
e.send_keys("Python")

text = driver.find_element(By.ID, "fdsfsdgdsg").text
assert "Python" in text, f'Expected Python to be in {text}'


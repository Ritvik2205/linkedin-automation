from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from os import getenv
from dotenv import load_dotenv

load_dotenv()

TAG_NAME = "tag name"

cService = webdriver.ChromeService(executable_path=getenv("EXECUTABLE_PATH"))
driver = webdriver.Chrome(service=cService)
driver.get("https://www.linkedin.com")
time.sleep(2)

#                                               Log in the user
# my_username = input("Username: ").strip()
# my_password = input("Password: ").strip()

# ******* temp constants
my_username = getenv('MY_USERNAME')
my_password = getenv('MY_PASSWORD')

username = driver.find_element("xpath", "//input[@name='session_key']")
password = driver.find_element("xpath", "//input[@name='session_password']")

username.send_keys(f"{my_username}")
password.send_keys(f"{my_password}")
time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']").click()


#                                               Adding contact list
# for i in range(100):
driver.get(f"https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=1&sid=oxuv")
time.sleep(3)

buttons_all = driver.find_elements(By.TAG_NAME, "button")

connect_buttons = [button for button in buttons_all if button.text == "Connect"]

for button in connect_buttons:
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    send_btn = driver.find_element("xpath", "//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send_btn)
    dismiss_btn = driver.find_element("xpath", "//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", dismiss_btn)
    time.sleep(2)

    # time.sleep(3)
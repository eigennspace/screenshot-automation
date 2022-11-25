from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import yaml

cred = yaml.safe_load(open('loginDetails.yml'))
userName = cred['credentials']['Username']
password = cred['credentials']['Password']

driver = webdriver.Chrome()

def login(url, usernameId, username, passwordId, password, submit_buttonId):
  driver.get(url)
  driver.find_element(By.ID, usernameId).send_keys(username)
  driver.find_element(By.ID, passwordId).send_keys(password)
  driver.find_element(By.CLASS_NAME, submit_buttonId).click()

login("https://117.102.85.20:8443/my.policy", "input_1", userName, "input_2" ,password, "credentials_input_submit")

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."

# get the errors (if there are)
errors = driver.find_elements(By.CLASS_NAME,"flash-error")

# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
from selenium import webdriver
from selenium.webdriver.common.by import By
from open_chrome_driver import open_chrome_driver
import time, getpass

def login_COOL(driver):
    driver.get("https://cool.ntu.edu.tw/login/portal")

    username = input("Username:")
    password = getpass.getpass("Password:")

    fail = True
    while fail:
        try:
            fail = False
            driver.find_element(By.CLASS_NAME, "css-qxdwt4-view--block-baseButton").click()
            time.sleep(1)
            driver.find_element(By.ID, "ContentPlaceHolder1_UsernameTextBox").send_keys(username)
            driver.find_element(By.ID, "ContentPlaceHolder1_PasswordTextBox").send_keys(password)
            driver.find_element(By.ID, "ContentPlaceHolder1_SubmitButton").click()
        except:
            fail = True
            print("Login FAIL! Retry...")

if __name__ == '__main__':
    driver = open_chrome_driver()
    login_COOL(driver)

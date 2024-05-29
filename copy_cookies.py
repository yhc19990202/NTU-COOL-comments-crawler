import requests
from selenium import webdriver

def copy_cookies(session, driver):
	selenium_user_agent = driver.execute_script("return navigator.userAgent;")
	session.headers.update({"user-agent": selenium_user_agent})
	for cookie in driver.get_cookies():
		session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
	return session

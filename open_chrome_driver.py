from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def open_chrome_driver():
    service = Service()
    chrome_options = Options()
    print("-----")
    print(chrome_options)
    print("-----")
    chrome_options.add_argument("--window-size=1920,1080")
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(service = service, options=chrome_options)
    return driver

if __name__ == '__main__':
    driver = open_chrome_driver()
    driver.get("https://www.google.com")

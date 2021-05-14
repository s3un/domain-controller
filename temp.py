from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


WINDOW_SIZE = "1920,1080"
options = Options()  
options.add_argument("--headless")  
options.add_argument("--window-size=%s" % WINDOW_SIZE)

domain = input("Enter your domain$ ")
output= input("Enter Output File Name$ ")
driver = webdriver.Chrome(options=options)
driver.get(domain)
driver.set_page_load_timeout(20)
driver.get_screenshot_as_file(output+'.png')
print("[+] Screenshot Saved")

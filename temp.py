from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("https://python.org")
sleep(1)
browser.get_screenshot_as_file("new.png")
browser.quit()



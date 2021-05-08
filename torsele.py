import time
from tbselenium.tbdriver import TorBrowserDriver
driver = TorBrowserDriver("//whoami/Desktop/seun/tor-browser_en-US/") 
driver.get('https://check.torproject.org')

time.sleep (60)
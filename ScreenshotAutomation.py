from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-ax-menu-list")
driver = webdriver.Chrome(chrome_options=chrome_options)

def getScreenshot_Indices():
  driver.get('http://10.100.112.209:5601/app/monitoring#/overview?_g=(cluster_uuid:tS11PnWbT4KL7XG2TPeBpg,refreshInterval:(pause:!f,value:10000),time:(from:now-15m,to:now))')
  sleep(15)
  driver.get_screenshot_as_file("screenshot.png")

getScreenshot_Indices()
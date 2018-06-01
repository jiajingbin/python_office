from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.8.13:9090")
sleep(3)
#ActionChains(driver).move_by_offset(0,0).context_click().perform()
#sleep(5)
ActionChains(driver).move_by_offset(520,120).context_click().perform()
sleep(5)
ActionChains(driver).move_by_offset(20,100).context_click().perform()

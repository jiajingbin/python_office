#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.8.11:9090")
driver.find_element_by_id("username").send_keys("safeadmin")

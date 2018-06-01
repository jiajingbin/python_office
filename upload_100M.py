#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import login
from login import *
import os
driver.find_element_by_xpath('//*[@id="navtab3"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="subnav3"]').click()
sleep(3)
#ActionChains(driver).move_by_offset(-350,-205).click().perform()
driver.switch_to.frame("submain_ifm")
driver.find_element_by_xpath("/html/body/div/div[1]/div/a[1]/span/span").click()
driver.switch_to.parent_frame()
sleep(3)
driver.switch_to.frame("submain_ifm")
sleep(3)
driver.find_element_by_xpath('//*[@id="displayName"]').send_keys("test")
driver.find_element_by_xpath('//*[@id="productVersion"]').send_keys("test")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/table[2]/tbody/tr[1]/td[2]/a/div[2]/label").click()
sleep(3)
os.system(r'"C:\Program Files\AutoIt3\project\upload_eng.exe"')
sleep(25)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[1]/div").click()

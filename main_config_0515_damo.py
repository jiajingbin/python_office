#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import login
from login import *
import os
from basic_scripts import *
#策略管理
driver.find_element_by_xpath('//*[@id="navtab3"]').click()
sleep(2)
#主机监控与审计
driver.find_element_by_xpath('//*[@id="subnav3"]').click()
#主机配置策略
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[2]").click()
sleep(2)
driver.switch_to.frame("submain_ifm")
sleep(2)

driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[9]/div/img").click()

status=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[9]/div/img")
print(status.get_attribute('src'))

table = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table")
print(table)
print(table.text)
all_table = [table_.text]

'''

all_data = driver.find_elements_by_xpath( "//div[@class='datagrid-cell datagrid-cell-c1-status']")
for i in all_data:
    print(i)
    print(i.text)
    
rowall = [rowall for rowall in all_data]
print("rowall:")
print(rowall)

rowall_text = [rowall_text.text for rowall_text in all_data]
print("rowall_text:")
print(rowall_text)
'''

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import login
from login import *
import os
from basic_scripts import *

#策略管理click
driver.find_element_by_xpath('//*[@id="navtab3"]').click()
sleep(2)
#主机监控与审计click
driver.find_element_by_xpath('//*[@id="subnav3"]').click()
sleep(2)
#主机配置策略click
driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[2]").click()
sleep(2)
#切换frame
driver.switch_to.frame("submain_ifm")
#删除多余策略 字符串需含有add的空策略
sleep(3)
clean_policy(policy_name_elements)
#新建策略
new_policy()
print(policyname)
#status_click(client_ip, policy_name_elements, status_elements)
checkbox(client_ip, policy_name_elements)

"""
##下发范围
#点击范围
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/div/img").click()
sleep(2)
#勾选复选框
checkbox(client_ip, ip_elements)
#save click
driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/a[1]/span/span").click()
#driver.switch_to.parent_frame()
"""




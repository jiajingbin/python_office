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

sleep(3)
clean_all_policy(policy_name_elements)

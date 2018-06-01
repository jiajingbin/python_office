#coding=utf-8
from selenium.webdriver.common.keys import Keys
from login_home import *
from basic_scripts import *
from time import sleep
#策略管理
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="navtab3"]'))).click()
#主机监控与审计
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="subnav3"]'))).click()
#主机配置策略
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div[3]/div[3]/div[2]"))).click()
#切换frame
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("submain_ifm"))
#清除多余策略7
clean_all_policy()
#新建策略
new_policy()
#范围
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/div/img"))).click()
#选择ip
checkbox(client_ip, ip_elements)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div[2]/a[1]/span/span"))).click()
#使能策略
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[9]/div/img"))).click()

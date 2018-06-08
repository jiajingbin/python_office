#coding=utf-8
from selenium.webdriver.common.keys import Keys
from login_home import *
from basic_scripts import *
from time import sleep
#策略管理
sleep(3)



confirm_check.mainpage_confirm(main_page_element, main_page_key_word, main_page_location)
'''
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("submain_ifm"))
tmp=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]"))).text
print(tmp)
sleep(0.5)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="navtab3"]'))).click()
#主机监控与审计
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import win32api
import win32con
#import pytesseract
#from PIL import Image
import os
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.8.13:9090")

def username_get():
    driver.find_element_by_id("username").send_keys("safeadmin")
def passwd_get():
    driver.find_element_by_id("password").send_keys("wst!@#$1234")
def validatecode_get():
    right_click = driver.find_element_by_xpath(".//*[@id='prtImg']")
    ActionChains(driver).context_click(right_click).send_keys(Keys.ARROW_DOWN).perform()
    win32api.keybd_event(86,win32con.KEYEVENTF_KEYUP,0)
    sleep(3)
    win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(89,win32con.KEYEVENTF_KEYUP,0)
def validatecode_tesseract():
    os.system("C:\\Users\win7\AppData\Local\Programs\Python\Python36-32\project\save.bat")
    f=open('C:\\Users\win7\Downloads\GetVerifyCode.do.txt')
    num=f.read()
    print(num)
    f.close
    return num

username_get()
passwd_get()
validatecode_get()
sleep(3)
validatecode = validatecode_tesseract()
print(validatecode)
driver.find_element_by_id("validateCode").send_keys(validatecode)
sleep(1)
driver.find_element_by_class_name("login_btn_out").click()

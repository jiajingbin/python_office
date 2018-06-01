from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import win32api
import win32con
import pytesseract
from PIL import Image
from pytesseract import *
from public import Login


    
class LoginTest():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.8.13:9090")
    def validatecode_cal(self):
        right_click = self.driver.find_element_by_xpath(".//*[@id='prtImg']")
        ActionChains(self.driver).context_click(right_click).send_keys(Keys.ARROW_DOWN).perform()
        win32api.keybd_event(86,win32con.KEYEVENTF_KEYUP,0)
        sleep(3)
        win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(89,win32con.KEYEVENTF_KEYUP,0)
    #def validatecode_pytesseract(self):
        rep={'O':'0',                           #替换列表
        'I':'1','L':'1',
        'Z':'2',
        'S':'8'
        };

        def initTable(threshold=140):           # 二值化函数
            table = []
            for i in range(256):
                if i < threshold:
                    table.append(0)
                else:
                    table.append(1)
            return table
        #--------------------------------------------------------------------------------------
        im = Image.open('C:\\Users\win7\Downloads\GetVerifyCode.do.gif')     #1.打开图片
        im = im.convert('L')                                        #2.将彩色图像转化为灰度图
        binaryImage = im.point(initTable(), '1')                    #3.降噪，图片二值化
        # binaryImage.show()
        vcode = image_to_string(binaryImage, config='-psm 7')
        #4.对于识别结果，常进行一些替换操作
        for r in rep:
            vcode = vcode.replace(r,rep[r])
        #5.打印识别结果
        print (vcode)
        return vcode
        
    def test_sysadmin_login(self):
        username = 'sysadmin'
        password = 'wst!@#$1234'
        Login().user_login(self.driver, username, password, validatecode)

LoginTest().validatecode_cal()

LoginTest().test_sysadmin_login()

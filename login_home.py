# coding=utf-8
import win32api,win32con
from pytesseract import *
from PIL import Image
from error import *
from basic_scripts import *
#from selenium import webdriver
#driver = webdriver.Firefox()
#driver.get("http://192.168.8.98:9090")
def username_get():
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'username'))).send_keys("safeadmin")
def passwd_get():
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'password'))).send_keys("wst!@#$1234")
def validatecode_get():
    driver.save_screenshot('E:\\printscreen.png')
    imgelement = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='prtImg']")))
    location = imgelement.location  # 获取验证码x,y轴坐标 
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open("E:\\printscreen.png")  # 打开截图
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('E:\\save.png') # 保存我们接下来的验证码图片 进行打码
def validatecode_pytesseract():
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
    im = Image.open("E:\\save.png")     #1.打开图片
    im = im.convert('L')                                        #2.将彩色图像转化为灰度图
    binaryImage = im.point(initTable(), '1')                    #3.降噪，图片二值化
    # binaryImage.show()
    vcode = image_to_string(binaryImage, config='-psm 7')
    #4.对于识别结果，常进行一些替换操作
    for r in rep:
        vcode = vcode.replace(r,rep[r])
    #5.打印识别结果
    return vcode
#输入密码
try:
    passwd_get()
except BaseException:
    print(passwd_error())
    win32api.MessageBox(0, passwd_error(), "TimeoutException",win32con.MB_OK)
    driver_quit()
#输入用户名
try:
    username_get()
except BaseException:
    print(username_error())
    win32api.MessageBox(0, username_error(), "TimeoutException",win32con.MB_OK)
    driver_quit()
#截图
try:
    validatecode_get()
except BaseException:
    print(validatecode_get_error())
    win32api.MessageBox(0, validatecode_get_error(), "ERROR！",win32con.MB_OK)
    driver_quit()
#获取验证码
validatecode = validatecode_pytesseract()
#输入验证码
try:
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'validateCode'))).send_keys(validatecode)
except BaseException:
    print(validatecode_error())                                                                             
    win32api.MessageBox(0, validatecode_error(), "TimeoutException！",win32con.MB_OK)
    driver_quit()
#点击登录
try:
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'login_btn_out'))).click()
except BaseException:
    print(login_btn_error())
    win32api.MessageBox(0, login_btn_error(), "TimeoutException！",win32con.MB_OK)
    driver_quit()
#验证是否登陆成功
try:
    WebDriverWait(driver,3).until(EC.title_is(u"卫士通综合安全管理系统"))
    print(u"登陆成功!")
#出错信息处理
except BaseException:
    errorinfo=driver.find_element_by_id("errorinfo").text
    if errorinfo == "login failure!reason : username is not existed":
        print(login_failure_username())
        win32api.MessageBox(0, login_failure_username(), "ERROR！",win32con.MB_OK)
    elif "login failure!reason : password is not corrected" in errorinfo:
        print(login_failure_passwd())
        win32api.MessageBox(0, login_failure_passwd(), "ERROR！",win32con.MB_OK)
    elif errorinfo == "login failure!reason : validate code is not corrected":
        print(login_failure_validatecode())
        win32api.MessageBox(0, login_failure_validatecode(), "ERROR！",win32con.MB_OK)
    else:
        print("unable log in, please check by mannal")

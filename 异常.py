'''
import tkinter.messagebox

try:
    fileContent = open("abnormal.txt")
    fileContent.close()
    print("over")
#把异常消息赋予一个"ex"变量
except Exception as ex:
    print(ex)
    tkinter.messagebox.showinfo("Alert",ex)
    tkinter.messagebox.askyesnocancel("askyesnocancel","Error Message:\n%s"%ex)
    #tkinter.messagebox.showinfo("showinfo","Error Message:\n%s"%ex)
    #tkinter.messagebox.showwarning("showwarning","Error Message:\n%s"%ex)
   # tkinter.messagebox.showerror("showerror","Error Message:\n%s"%ex)
   # tkinter.messagebox.askquestion("askquestion","Error Message:\n%s"%ex)
    #tkinter.messagebox.askokcancel("askokcancel","Error Message:\n%s"%ex)
    #tkinter.messagebox.askretrycancel("askretrycancel","Error Message:\n%s"%ex)
    
'''
#-*-coding=utf-8
 
from selenium import webdriver
 
import unittest
 
 
 
class login(unittest.TestCase):
 
    def setUp(self):
 
        self.driver = webdriver.Firefox()
 
        self.driver.implicitly_wait(30)
 
        self.base_url = "http://www.baidu.com"
 
        self.verificationErrors = []
 
    
 
    def test_loginpass(self):
 
        driver = self.driver
 
        driver.get(self.base_url)
 
        nowhandle=driver.current_window_handle#在这里得到当前窗口句柄
 
        driver.find_element_by_id("kw").send_keys("selenium")
 
        driver.find_element_by_id("su").click()
 
        driver.find_element_by_xpath("//a[@title='selenium 安装']").click()
 
        aalhandles=driver.window_handles#获取所有窗口句柄
 
        for handle in aalhandles:#在所有窗口中查找弹出窗口
 
            if handle!=nowhandle:
 
                driver.switch_to_window(handle)#这两步是在弹出窗口中进行的操作，证明我们确实进入了
 
                driver.find_element_by_link_text("新闻").click()
 
        driver.switch_to_window(nowhandle)#返回到主窗口页面
 
        driver.find_element_by_id("kw").clear()#下面三步是返回到主窗口中进行的操作，证明我们确实返回了
 
        driver.find_element_by_id("kw").send_keys("python")
 
        driver.find_element_by_id("su").click()
 
        
 
    def tearDown(self):
 
        #self.driver.quit()
 
        self.assertEqual([], self.verificationErrors)
 
 
 
if __name__ == "__main__":
 
    unittest.main()

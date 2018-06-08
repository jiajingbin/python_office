#coding=utf-8
from selenium.webdriver.common.keys import Keys
from login_home import *
from basic_scripts import *
from time import sleep
#策略管理
sleep(0.5)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="navtab3"]'))).click()
#主机监控与审计
sleep(0.5)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="subnav3"]'))).click()
#主机配置策略
sleep(0.5)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div[3]/div[3]/div[2]"))).click()
#切换frame
sleep(0.5)
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("submain_ifm"))
sleep(0.5)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/div/img"))).click()
#选择ip
sleep(3)


table_search(client_ip)

checkbox_click(ip_elements)

'''
def table_search(ip):
    #定位table
    table = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/table")
    #table的总行数，不含标题
    table_rows = table.find_elements_by_tag_name('tr')
    #print("总行数:",len(table_rows))
    #tabler的总列数

    #在table中找到第一个tr,之后在其下找到所有的td,即是tabler的总列数

    table_cols = table_rows[0].find_elements_by_tag_name('td')
    #print("总列数:",len(table_cols))
    #按页扫描IP，每页默认10个ip，如扫描不到，切换下一页
    for i in range(0,len(table_rows)):
        row_col = table_rows[i].find_elements_by_tag_name('td')[1].text
        list_ip.append(row_col)
    for i in range(0,len(table_rows)):
        row_col = table_rows[i].find_elements_by_tag_name('td')[1].text
        while ip not in list_ip:
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[10]/a/span/span/span"))).click()
            print(ip_search_error())
            win32api.MessageBox(0, ip_search_error(), "ERROR！",win32con.MB_OK)
            return 0
        else:
            if row_col == ip:
                print("ip in")
                global ip_index
                ip_index = i
                return ip_index
        #print("第二列的text:",row_col)
'''

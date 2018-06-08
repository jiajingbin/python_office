#coding=utf-8
import paramiko
import datetime  
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import win32api,win32con
from time import sleep
from error import *

##ssh remote
xserver_ip = "192.168.8.98"
xserver_port = 22
xserver_username = "wst"
xserver_passwd = "1"
server_addr = "http://%s:9090" %xserver_ip

client_port = 22
client_username = "wst"
client_passwd = "1"

file_local_dir = r'D:\autotest'
file_remote_dir = r'/home/wst/autotest/'

driver = webdriver.Firefox()
driver.get(server_addr)

#main_config
policyName="test"
client_ip="192.168.8.245"
client_port = 22
client_username = "wst"
client_root = "root"
client_root_psd = "ssssssssrmxarmeueamf011"
client_passwd = "1"
main_config_cmd = ["cd /home/wst/   ","pwd"]




#全局变量
ip_index = 0
list_ip = []

#超时检测
main_page_element = "/html/body/div[2]/div[2]/div/div[1]/div[1]/div[1]"
main_page_key_word = u"违规事件"
main_page_location = "main_page"

ip_are_element = "/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/span[1]"
ip_are_key_word = u"终端IP"
ip_are_location = "ip_are"

class confirm_check():
    def mainpage_confirm(confirm_element, key_word ,location):
        start = time.clock()
        #driver.switch_to.frame("submain_ifm")
        #WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("submain_ifm"))
        tmp = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,confirm_element))).text
        while tmp != key_word:
            print("持续检测中......")
            sleep(1)
            tmp = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,confirm_element))).text
            #tmp = driver.find_element_by_xpath(confirm_element).text
            end = time.clock()
            if int(end - start) == 10:
                print("Warning: %s Time Out:10s" %location)
                win32api.MessageBox(0, check_error(), location, win32con.MB_OK)
                break
        else:
            print("confirm!")
            return 0
    def policy_manage_confirm():
        pcy_addr = "%s/PolicyIndex.do" %server_addr
        while driver.current_url != pcy_addr:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="navtab3"]'))).click()
        else:
            print("policy_manage_confirm OK")
            return 0
    def audit_sys_confirm():
        locate_nav = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="subnav3"]'))).get_attribute("class")
        while locate_nav != "subnav_selected":
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="subnav3"]'))).click()
            locate_nav = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="subnav3"]'))).get_attribute("class")
        else:
            print("audit_sys_confirm OK")
            return 0
    def main_cfg_confirm():
        locate_nav = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[3]/div[3]/div[2]"))).text
        print(locate_nav)
        while locate_nav != "主机配置策略":
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[3]/div[3]/div[2]"))).click()
            locate_nav = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[3]/div[3]/div[2]"))).text
        else:
            print("main_cfg_confirm OK")
            return 0


#quit driver
def driver_quit():
    driver.quit()
    sys.exit(0)
####
#session_confirm
def checkboxtest(ip, elements):
    print(u"正在选择被测终端......")
    sleep(4)
    utl=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/span[1]")))
    if utl.text == "终端IP":
        ip_arrays = driver.find_elements_by_xpath(elements)
        print(ip_arrays.text)
        #print(ip_arrays)
        ip_array = [ip_array.text for ip_array in ip_arrays]
        print(ip_array)
        if ip in ip_array:
            ip_index_1=ip_array.index(ip)
            print("ip_index_1:" %ip_index)
        else:
            print("%s is not in server_ip_list " %ip)
            return 0
        ip_index=ip_index_1-1
        print("ip_index:" %ip_index)
        checkboxes=driver.find_elements_by_xpath(checkbox_elements)
        checkbox = [i for i in checkboxes if i.get_attribute("name") == "username"]
        session = checkbox[ip_index]
        #sleep(3)
        for i in checkboxes:
            if i == session:
                if i.is_selected() == False:                
                    i.click()
                    print(u"选择完毕!")
####

#policy_name_elements
policy_name_elements = "//div[@class='datagrid-cell datagrid-cell-c1-policyName']"
#domain_name_elements
domain_name_elements = "//div[@class='datagrid-cell datagrid-cell-c1-domain']"
#status_elements
status_elements = "//div[@class='datagrid-cell datagrid-cell-c1-status']"
#status_click
def status_click(ip, elements1, elements2):
    ip_arrays = driver.find_elements_by_xpath(elements1)
    ip_array = [ip_array.text for ip_array in ip_arrays]
    print(ip_array)
    for i in ip_array:
        if ip in i:
            ip_index=ip_array.index(i)
            status_arrays = driver.find_elements_by_xpath(elements2)
            status_array = [status.text for status in status_arrays]
            print(status_array)
            return 0

    '''
    #ip_index=ip_index_1-1
    checkboxes=driver.find_elements_by_xpath(checkbox_elements)
    checkbox = [i for i in checkboxes if i.get_attribute("name") == "username"]
    session = checkbox[ip_index]
    sleep(3)
    for i in checkboxes:
        if i == session:
            if i.is_selected() == False:                
                i.click()
    '''


#新建策略
def new_policy():
    ##判断策略名是否存在，如存在，结尾加字符串新命名
    #提取所有策略名    
    all_policynames = driver.find_elements_by_xpath( "//div[@class='datagrid-cell datagrid-cell-c1-policyName']")
    #切换成数组
    policy_arrays = [i.text for i in all_policynames]
    policyname= policyName
    while policyname in policy_arrays:
        policyname = policyname+"add"
    
    #新增策略click
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/a[1]/span/span"))).click()
    #driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/a[1]/span/span").click()
    #确定click
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[9]/div[2]/div[2]/a[1]/span/span"))).click()
    #driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[2]/a[1]/span/span").click()
    #策略名输入
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="policyName"]'))).send_keys(policyname)
    #driver.find_element_by_xpath('//*[@id="policyName"]').send_keys(policyname)
    #Save click
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[1]/div"))).click()
    print(u"新建策略完成!")
    return policyname


#checkboxes
checkbox_elements = "//input[@type='checkbox']"
#checkbox
ip_elements = "//div[@class='datagrid-view2']"
#ssh connect
ssh = paramiko.SSHClient()
def ssh_connect(ip, port, user, passwd):
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, user, passwd, timeout=3)
    except:
        print("ssh_connect err.")

#ssh command
def ssh_cmd(cmd):
    result = ""
    try:
        stdin, stdout, stderr =ssh.exec_command(cmd)
        result = stdout.read()
        print(result)
    except:
        print("ssh_cmd err.")
    return result

#ssh close
def ssh_close():
    ssh.close

#file upload
def upload(local_dir,remote_dir):
    try:
        t=paramiko.Transport((client_ip,client_port))
        t.connect(username=client_username,password=client_passwd)
        sftp=paramiko.SFTPClient.from_transport(t)
        print ('upload file start %s ' % datetime.datetime.now())
        for root,dirs,files in os.walk(local_dir):
            for filespath in files:
                local_file = os.path.join(root,filespath)
                a = local_file.replace(local_dir,'').replace('\\','/').lstrip('/')
                remote_file = os.path.join(remote_dir,a)
                try:
                    sftp.put(local_file,remote_file)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file,remote_file)
                print ("upload %s to remote %s" % (local_file,remote_file))
            for name in dirs:
                local_path = os.path.join(root,name)
                a = local_path.replace(local_dir,'').replace('\\','') 
                remote_path = os.path.join(remote_dir,a)
                try:
                    sftp.mkdir(remote_path)
                    print ("mkdir path %s" % remote_path)
                except Exception as e:
                    print(e)
        print('upload file success %s ' % datetime.datetime.now())
        print(u"上传成功!")
        t.close()
    except Exception as e:
        print(e)

#file download
def file_download(remote_path,local_path):  
    t = paramiko.Transport((xserver_ip,xserver_port))  
    t.connect(username=xserver_username, password=xserver_passwd)  
    sftp = paramiko.SFTPClient.from_transport(t)
    try:
        print ('download file start %s ' % datetime.datetime.now())
        sftp.get(remote_path,local_path)
        print ("download %s to remote %s" % (remote_path,local_path))
    except Exception as e:
        print(e)
    print('download file success %s ' % datetime.datetime.now())
    t.close()


#session_confirm
def checkbox(ip, elements):
    print(u"正在选择被测终端......")
    sleep(4)
    utl=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/span[1]")))
    if utl.text == "终端IP":
        ip_arrays = driver.find_elements_by_xpath(elements)
        #print(ip_arrays)
        ip_array = [ip_array.text for ip_array in ip_arrays]
        print(ip_array)
        if ip in ip_array:
            ip_index_1=ip_array.index(ip)
        else:
            print("%s is not in server_ip_list " %ip)
            return 0
        ip_index=ip_index_1-1
        checkboxes=driver.find_elements_by_xpath(checkbox_elements)
        checkbox = [i for i in checkboxes if i.get_attribute("name") == "username"]
        session = checkbox[ip_index]
        #sleep(3)
        for i in checkboxes:
            if i == session:
                if i.is_selected() == False:                
                    i.click()
                    print(u"选择完毕!")
#ip定位
def table_search(ip):
    #定位table
    table = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/table")
    #table的总行数，不含标题
    table_rows = table.find_elements_by_tag_name('tr')
    #tabler的总列数
    #在table中找到第一个tr,之后在其下找到所有的td,即是tabler的总列数
    table_cols = table_rows[0].find_elements_by_tag_name('td')
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
                global ip_index
                ip_index = i
                return ip_index

#根据table_search_ip点击复选框
def checkbox_click(elements):
    print(u"正在选择被测终端......")
    checkbox_index=ip_index
    checkboxes=driver.find_elements_by_xpath(checkbox_elements)
    checkbox = [i for i in checkboxes if i.get_attribute("name") == "username"]
    session = checkbox[checkbox_index]
    for i in checkboxes:
        if i == session:
            if i.is_selected() == False:                
                i.click()
                print(u"选择完毕!")




                    
#clean policy
def clean_policy():
    policy_names = driver.find_elements_by_xpath(policy_name_elements)
    domain_names = driver.find_elements_by_xpath(domain_name_elements)
    checkboxes=driver.find_elements_by_xpath(checkbox_elements)
    policy_name_array = [i.text for i in policy_names]
    policy_name_array_no = [i for i in policy_names]
    domain_name_array = [i.text for i in domain_names]
    pcy_dom_array = list(map(lambda x,y:[x,y],policy_name_array,domain_name_array))
    len_pcy_dom = len(pcy_dom_array)
    for j in range(len_pcy_dom):
        if pcy_dom_array[j][1] == "尚未分配":
            if 'add' in pcy_dom_array[j][0]:
                policy_name_array_no[j].click()
    
    for k in checkboxes:
        if k.is_selected() == True:                
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/a[4]/span/span"))).click()
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[12]/div[2]/div[4]/a[1]/span/span"))).click()
            return 0
#删除所有含add的策略
def clean_all_policy():
    policy_names = driver.find_elements_by_xpath(policy_name_elements)
    domain_names = driver.find_elements_by_xpath(domain_name_elements)
    checkboxes = driver.find_elements_by_xpath(checkbox_elements)
    policy_name_array = [i.text for i in policy_names]
    policy_name_array_no = [i for i in policy_names]
    domain_name_array = [i.text for i in domain_names]
    pcy_dom_array = list(map(lambda x,y:[x,y],policy_name_array,domain_name_array))
    len_pcy_dom = len(pcy_dom_array)

    for j in range(len_pcy_dom):
        if 'add' in pcy_dom_array[j][0]:
            policy_name_array_no[j].click()
    
    for k in checkboxes:
        if k.is_selected() == True:                
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/a[4]/span/span"))).click()
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[12]/div[2]/div[4]/a[1]/span/span"))).click()
            return 0    



#scp

#if __name__=='__main__':  
#     local_dir=r'D:\upload11111'  
#     remote_dir='/home/wst/upload1111/'  
#     upload(local_dir,remote_dir)

#ssh

if __name__=='__main__':
    ssh_connect(client_ip, client_port, client_root, client_root_psd)
    ssh_cmd("cd /home/wst/autotest&&ls -al&&chmod +x *&&./main_config.sh ")
    ssh_cmd("pwd")
'''
if __name__ == '__main__':
    remote_path = '/home/wst/download123/123.txt'
    local_path = r'D:\download11111\123.txt'
    file_download(remote_path,local_path)
'''

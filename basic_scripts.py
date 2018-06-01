#coding=utf-8
import paramiko
import datetime  
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://192.168.8.98:9090")

#main_config
policyName="test"
client_ip="192.168.8.139"
main_config_cmd = ["cd /home/wst/upload1111","pwd"]
##ssh remote
xserver_ip = "192.168.8.98"
xserver_port = 22
xserver_username = "wst"
xserver_passwd = "1"
#quit driver
def driver_quit():
    driver.quit()
    sys.exit(0)
####
#session_confirm
def checkboxtest(ip, elements):
    ip_arrays = driver.find_elements_by_xpath(elements)
    ip_array = [ip_array.text for ip_array in ip_arrays]
    if ip in ip_array:
        ip_index_1=ip_array.index(ip)
    else:
        print("%s is not in server_ip_list " %ip)
        os._exit()
    ip_index=ip_index_1-1
    checkboxes=driver.find_elements_by_xpath(checkbox_elements)
    checkbox = [i for i in checkboxes if i.get_attribute("name") == "username"]
    session = checkbox[ip_index]
    sleep(3)
    for i in checkboxes:
        if i == session:
            if i.is_selected() == False:                
                i.click()
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
    print("新建策略完成")
    return policyname


#checkboxes
checkbox_elements = "//input[@type='checkbox']"
#checkbox
ip_elements = "//div[@class='datagrid-cell datagrid-cell-c2-ip']"
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
        t=paramiko.Transport((xserver_ip,xserver_port))
        t.connect(username=xserver_username,password=xserver_passwd)
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
    sleep(3)
    utl=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/span[1]")))
    if utl.text == "终端IP":
        ip_arrays = driver.find_elements_by_xpath(elements)
        print(ip_arrays)
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
        sleep(3)
        for i in checkboxes:
            if i == session:
                if i.is_selected() == False:                
                    i.click()
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
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/a[4]/span/span").click()
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[12]/div[2]/div[4]/a[1]/span/span").click()
            sleep(1)
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
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/a[4]/span/span"))).click()
            WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[12]/div[2]/div[4]/a[1]/span/span"))).click()
            return 0    

#scp

#if __name__=='__main__':  
#     local_dir=r'D:\upload11111'  
#     remote_dir='/home/wst/upload1111/'  
#     upload(local_dir,remote_dir)

#ssh
"""
if __name__=='__main__':
    ssh_connect(xserver_ip, xserver_port, xserver_username, xserver_passwd)
    ssh_cmd("cd upload1111&&pwd&&ls ")
    ssh_cmd("pwd")
"""
if __name__ == '__main__':
    remote_path = '/home/wst/download123/123.txt'
    local_path = r'D:\download11111\123.txt'
    file_download(remote_path,local_path)


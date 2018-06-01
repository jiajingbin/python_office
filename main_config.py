#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import login
from login import *
import os
test_ip="192.168.8.197"
driver.find_element_by_xpath('//*[@id="navtab3"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="subnav3"]').click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[2]").click()
sleep(2)

#driver.switch_to.frame("submain_ifm")
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/a[1]/span/span").click()
#driver.switch_to.parent_frame()

#sleep(2)
driver.switch_to.frame("submain_ifm")
#driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[2]/a[1]/span/span").click()
#sleep(2)
#driver.find_element_by_xpath('//div[@class="/images/table_beginspy.gif"]').click()

#a = driver.find_element_by_id("startRun").get_attribute("value")
#print(a)
#driver.find_element_by_id("policyName").send_keys("test")
#sleep(2)
#driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/div/img").click()
sleep(2)
table = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/table")
sleep(3)

all_data = driver.find_elements_by_xpath( "//div[@class='datagrid-cell datagrid-cell-c2-ip']")
for i in all_data:
    print(i)
    print(i.text)
    
rowall = [rowall for rowall in all_data]
print("rowall:")
print(rowall)

rowall_text = [rowall_text.text for rowall_text in all_data]
print("rowall_text:")
print(rowall_text)

if test_ip in rowall_text:
    ip_index_1=rowall_text.index(test_ip)
else:
    print("%s is not in server_ip_list " %test_ip)
    os._exit()
ip_index=ip_index_1-1
print("ip_index:")
print(ip_index)

checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
checkbox = [i for i in checkboxes if i.get_attribute("name") == "username"]
print("checkbox:")
print(checkbox[ip_index])
session = checkbox[ip_index]
#session = rowall[ip_index]
print("session:")
print(session)



all_check = [i for i in checkboxes]
print("all_check")
print(all_check)
print("check_index")
print(all_check.index(session))
checkbox_index = all_check.index(session)
print(checkbox_index)

count = len(checkboxes)
for i in checkboxes:
    print("i:")
    print(i)
    if i == session:
        if i.is_selected() == False:
            
            i.click()

"""
all_data = driver.find_elements_by_xpath( "//div[@class='datagrid-cell datagrid-cell-c2-ip']")
#all_data = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/table").find_elements_by_tag_name("tr")
for i in all_data:
    print("all_data:")
    print(i)
    print(i.text)
    
rowall = [rowall.text for rowall in all_data]
print("rowall:")
print(rowall)
rowall1 = [rowall1 for rowall1 in all_data]
print("rowall1:")
print(rowall1)
'''
if test_ip in rowall:
    ip_index=rowall.index(test_ip)
else:
    print("%s is not in server_ip_list " %test_ip)
    os._exit()
'''
print("ip_index:")
print(ip_index)

checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
all_check = [i for i in checkboxes]
print("all_check")
print(all_check)

checkbox = [i for i in checkboxes if i.get_attribute("name") == "username"]
print("checkbox:")
print(checkbox)

checkbox1 = [i.text for i in checkboxes if i.get_attribute("name") == "username"]
print("checkbox1:")
print(checkbox1)
'''
for i in checkboxes:
    if i.get_attribute("name") == "username":
        print("true")
'''
#if driver.find_elements_by_xpath("//input[@type='checkbox']").get_attribute("name") == "username":
#    print("checkboxes=",len(checkboxes))
#rowindex = [rowall.index(i) for i in rowall if "192.168.8.239" in i]
#print(rowindex)



'''
trlist = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/table").find_elements_by_tag_name("tr")
for tr in trlist:
    tdlist = tr.find_elements_by_tag_name("td")
    if len(tdlist)>0:
        text=tdlist[1].text
        if text == "192.168.8.239":
            print(tdlist[2].text)
'''
'''
#all rows
table_rows = table.find_elements_by_tag_name("tr")
print("all rows=",len(table_rows))
#all cols
table_cols = table_rows[0].find_elements_by_tag_name('td')
print("all cols=",len(table_cols))
for tr in table_rows:
    if len(table_cols)>0:
        
ips = table_rows[1].find_elements_by_tag_name('td')[1].text
print(ips)
#for ip in ips:
#    print(ip)
'''
"""

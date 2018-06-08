#coding=utf-8
from login_home import *
from basic_scripts import *
#策略管理
#先确认标签再点击
confirm_check.policy_manage_confirm()
#主机监控与审计
confirm_check.audit_sys_confirm()
#主机配置策略
confirm_check.main_cfg_confirm()
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[3]/div[3]/div[2]"))).click()
#切换frame
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("submain_ifm"))
#清除多余策略
clean_all_policy()
#新建策略
new_policy()
#范围
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/div/img"))).click()
#选择ip
sleep(5)
#confirm_check.mainpage_confirm(ip_are_element, ip_are_key_word, ip_are_location)
table_search(client_ip)
checkbox_click(ip_elements)
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[6]/div[2]/div[2]/a[1]/span/span"))).click()
#如未成功，再次定位
client_ip_tmp = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[6]/div/div/nobr"))).text
while client_ip not in client_ip_tmp: 
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[7]/div/img"))).click()
    table_search(client_ip)
    checkbox_click(ip_elements)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[6]/div[2]/div[2]/a[1]/span/span"))).click()
#使能策略
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[9]/div/img"))).click()
print(u"策略使能完成!")
#上传脚本
upload(file_local_dir,file_remote_dir)
#执行脚本
ssh_connect(client_ip, client_port, client_root, client_root_psd)
ssh_cmd("cd /home/wst/autotest&&chmod +x *&&./main_config.sh ")
print("主机配置审计测试完成！")
#关闭策略
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[9]/div/img"))).click()

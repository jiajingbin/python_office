#import ssh
import paramiko
#from paramiko.transport import SecurityOptions, Transport
myclient = paramiko.SSHClient()
myclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
myclient.connect("192.168.8.26",port=22,username="wst",password="1")
stdin,stdout,stderr = myclient.exec_command("ls -l")
print (stdout.read())


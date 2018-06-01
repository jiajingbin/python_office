import paramiko  
def remote_scp(host_ip,remote_path,local_path,username,password):  
    t = paramiko.Transport((host_ip,22))  
    t.connect(username=username, password=password)  
    sftp = paramiko.SFTPClient.from_transport(t)  
    src = remote_path  
    des = local_path  
    sftp.get(src,des)  
    t.close()  
  
  
if __name__ == '__main__':
    host_ip = '192.168.8.98'
    remote_path = '/home/wst/download123/123.txt'
    local_path = r'D:\download11111\123.txt'
    username = 'wst'
    password = '1'
    remote_scp(host_ip,remote_path,local_path,username,password)

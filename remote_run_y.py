import paramiko
def ssh_cmd(ip, port, cmd, user, passwd):

    result = ""

    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, user, passwd, timeout=3)
        stdin, stdout, stderr =ssh.exec_command(cmd)
        result = stdout.read()
        print(result)
        ssh.close()
    except:
        print("ssh_cmd err.")
    return result
ssh_cmd("192.168.8.98","22","cd ~","wst","1")
ssh_cmd("192.168.8.98","22","touch 123321","wst","1")
ssh_cmd("192.168.8.98","22","echo 123321 >> 123321","wst","1")
ssh_cmd("192.168.8.98","22","cat 123321","wst","1")
ssh_cmd("192.168.8.98","22","ls -al","wst","1")

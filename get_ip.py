import request
import sys
import socket

def get_ip(url):
    if 'http' in str(url):
        url = url.split('//')[1]
        ip = socket.gethostbyname(url)
    else:
        ip = socket.gethostbyname(url)
    return ip
get_ip()

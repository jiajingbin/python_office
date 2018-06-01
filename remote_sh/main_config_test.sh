#!/bin/bash
if [ -f /usr/lib64/mozilla/plugins/a.so ];then
	rm -rf /usr/lib64/mozilla/plugins/a.so
	touch /usr/lib64/mozilla/plugins/a.so
	chmod +x /usr/lib64/mozilla/plugins/a.so

service sshd restart
service sshd stop
service sshd start

if [ -f /etc/profile ];then
	echo "echo test_main_config" >> /etc/profile
	sed - i '$d' /etc/profile
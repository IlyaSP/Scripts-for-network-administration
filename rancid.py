# -*- coding: utf-8 -*-

import re
import sys
import os


if os.path.isfile("/etc/hosts"):
	pass
else:
	print('=====# File "/etc/hosts" not found #=====\r\n')
	exit.sys()

	
if os.path.isfile("/var/rancid/Networking/router.db"):
	pass
else:
	print('=====# /var/rancid/Networking/router.db #=====\r\n')
	exit.sys()

	
k = 0
while k != 4:
    ip = raw_input("Enter the ip address: ")
    if re.search(r'\d+.\d+.\d+.\d+', ip) is not None:
        ip_test = ip.split(".")
        for i in ip_test:
            if int(i) >= 0 and int(i) < 256:
                k += 1
                continue
            else:
                print("address error")
                k = 0
                break
    else:
        print("address error")
        k = 0


hostname = raw_input("Enter the hostname: ")
status = 0
while (status != "up") and (status != "down"):
    status = raw_input("Enter device status(up/down): ")
    if (status != "up") and (status != "down"):
        print("status error")

print("\r\n##########################################################################################\r\n"
      "# Vendor compliance and database values below                                            #\r\n"
      "# Cisco IOS device: cisco\r\n# Cisco Nexus: cisco-nx\r\n# Cisco IOS-XR device: cisco-xr  #\r\n"
      "# Juniper device: juniper                                                                #\r\n"
      "##########################################################################################\r\n")

vendor = raw_input("Enter the device vendor: ")

print('Hostname: {0}\r\nIP: {1}\r\nStatus: {2}\r\nVendor: {3}\r\n'.format(hostname, ip, status, vendor))


data_correct = raw_input("The data is correct? (y/n): ")

if data_correct == "y":
	a = 0
	with open("/etc/hosts", "r") as hosts:
		for i in hosts:
			ip_host = i.split(" ")
			if str(ip_host[0].rstrip()) == ip:
				print("{0} ip address alredy exist in '/etc/hosts' \r\n".format(ip_host[0]))
				a = 1
				break
			elif str(ip_host[1].rstrip()) == hostname:
				print("{0} hostname alredy exist in '/etc/hosts' \r\n".format(ip_host[1].rstrip()))
				a = 1
				break
			else:
				continue
	if a == 0:
		with open("/etc/hosts", "a") as hosts:
			hosts.write("{0} {1}\n".format(ip, hostname))
		with open("/var/rancid/Networking/router.db", "a") as router_db:
			router_db.write("{0};{1};{2}\n".format(ip, vendor, status))
		print("##################################################\r\n"
			  "#  Device {0} {1} add in rancid          #\r\n"
			  "##################################################\r\n".format(hostname, ip))

			
else:
	print('=====# End work #=====\r\n')
	exit.sys()

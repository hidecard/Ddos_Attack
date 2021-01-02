#!/usr/bin/env python3

import subprocess

target = input("Input IP Address:  ")

	print("Attacking......")

	

DDOS = subprocess.run(['ping',target,'-l','65500','-w','1','-n','1'])

print('returncode:', DDOS.returncode)

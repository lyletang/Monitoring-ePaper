#!/usr/bin/env python
# coding: utf-8

'''
Project: Modular cloud computing cluster monitoring
Equipment: RaspberryPi 3B, 4.3inch-ePaper(Waveshare)
Author: Jiahui Tang
Date: 2017-6-11
'''

#import the necessary packages
import time
import datetime
import json
import os
import sys
import time

#import the own packages
from ePaper import *
from display import *

#define the IPs of nodes
master_ip = '192.168.2.32'
slave1_ip = '192.168.2.33'
slave2_ip = '192.168.2.34'
slave3_ip = '192.168.2.35'
slave4_ip = '192.168.2.36'

#define the bmp name
spark_bmp = 'SPARK.BMP'
raspberrypi_bmp = 'PI.BMP'
connect_failure_bmp = 'NO.BMP'

status = []

#connect to the 4.3inch-ePaper(UART)
screen_width = 800
screen_height = 600
screen = Screen('/dev/ttyAMA0') #if you use the USB-TTL, please replaced with '/dev/ttyACM0'
screen.connect()
screen.handshake()

#load font and pictures from the tf-card
#screen.load_font()
screen.load_pic()
#time.sleep(5)

#test the command
#screen.test()

#init the 4.3inch-ePaper
screen.clear()
screen.set_memory(MEM_FLASH)
screen.set_rotation(ROTATION_180)

#test display
'''
Display.time_(screen)
Display.logo_(screen)
Display.node_name_(screen)
Display.info_(screen, 'master')
Display.info_(screen, 'slave1')
Display.info_(screen, 'slave2')
Display.info_(screen, 'slave3')
Display.info_(screen, 'slave4')
'''

Display.time_(screen)
Display.logo_(screen)
Display.node_name_(screen)


def main():
	try:
		#try to connect to the master 
		ping_cmd = 'ping -c 1 -W 1 -v {ip_address}'.format(ip_address = master_ip)

		#if success
		if not os.system(ping_cmd):
			#test print
			print '[INFO] yes, master'
							
			username = 'pi'
			ip_address = master_ip
			command = 'python ~/monitor.py'

			cmd = 'rsh -l {username} {ip_address} {command}'.format(username = username, ip_address = ip_address, command = command)
			
			status = os.popen(cmd).read().split('\n')
			
			cpu_rate, memory_usage, total_time, cpu_temp, null_ = status

			cpu_rate = str("%.2f" % float(cpu_rate))
			memory_usage = str("%.2f" % float(memory_usage))
			total_time = str("%d" % float(total_time))
			cpu_temp = str("%d" % float(cpu_temp))

			print cpu_rate
			print memory_usage
			print total_time
			print cpu_temp

			Display.info_(screen, 'master', cpu_rate, memory_usage, total_time, cpu_temp)

		else:
			Display.connect_failure_(screen, 'master')

		#try to connect to the slave1
		ping_cmd = 'ping -c 1 -W 1 -v {ip_address}'.format(ip_address = slave1_ip)

		#if success
		if not os.system(ping_cmd):
			#test print
			print '[INFO] yes, s1'
		
			username = 'pi'
			ip_address = slave1_ip
			command = 'python ~/monitor.py'

			cmd = 'rsh -l {username} {ip_address} {command}'.format(username = username, ip_address = ip_address, command = command)
			
			status = os.popen(cmd).read().split('\n')
			
			cpu_rate, memory_usage, total_time, cpu_temp, null_ = status

			cpu_rate = str("%.2f" % float(cpu_rate))
			memory_usage = str("%.2f" % float(memory_usage))
			total_time = str("%d" % float(total_time))
			cpu_temp = str("%d" % float(cpu_temp))

			print cpu_rate
			print memory_usage
			print total_time
			print cpu_temp

			Display.info_(screen, 'slave1', cpu_rate, memory_usage, total_time, cpu_temp)

		else:
			Display.connect_failure_(screen, 'slave1')

		#try to connect to the slave2
		ping_cmd = 'ping -c 1 -W 1 -v {ip_address}'.format(ip_address = slave2_ip)

		#if success
		if not os.system(ping_cmd):
			#test print
			print '[INFO] yes, s2'

			username = 'pi'
			ip_address = slave2_ip
			command = 'python ~/monitor.py'

			cmd = 'rsh -l {username} {ip_address} {command}'.format(username = username, ip_address = ip_address, command = command)
			
			status = os.popen(cmd).read().split('\n')
			
			cpu_rate, memory_usage, total_time, cpu_temp, null_ = status

			cpu_rate = str("%.2f" % float(cpu_rate))
			memory_usage = str("%.2f" % float(memory_usage))
			total_time = str("%d" % float(total_time))
			cpu_temp = str("%d" % float(cpu_temp))

			print cpu_rate
			print memory_usage
			print total_time
			print cpu_temp

			Display.info_(screen, 'slave2', cpu_rate, memory_usage, total_time, cpu_temp)

		else:
			Display.connect_failure_(screen, 'slave2')

		#try to connect to the slave3
		ping_cmd = 'ping -c 1 -W 1 -v {ip_address}'.format(ip_address = slave3_ip)

		#if success
		if not os.system(ping_cmd):
			#test print
			print '[INFO] yes, s3'

			username = 'pi'
			ip_address = slave3_ip
			command = 'python ~/monitor.py'

			cmd = 'rsh -l {username} {ip_address} {command}'.format(username = username, ip_address = ip_address, command = command)
			
			status = os.popen(cmd).read().split('\n')
			
			cpu_rate, memory_usage, total_time, cpu_temp, null_ = status

			cpu_rate = str("%.2f" % float(cpu_rate))
			memory_usage = str("%.2f" % float(memory_usage))
			total_time = str("%d" % float(total_time))
			cpu_temp = str("%d" % float(cpu_temp))

			print cpu_rate
			print memory_usage
			print total_time
			print cpu_temp

			Display.info_(screen, 'slave3', cpu_rate, memory_usage, total_time, cpu_temp)

		else:
			Display.connect_failure_(screen, 'slave3')

		#try to connect to the slave4
		ping_cmd = 'ping -c 1 -W 1 -v {ip_address}'.format(ip_address = slave4_ip)

		#if success
		if not os.system(ping_cmd):
			#test print
			print '[INFO] yes, s4'

			username = 'pi'
			ip_address = slave4_ip
			command = 'python ~/monitor.py'

			cmd = 'rsh -l {username} {ip_address} {command}'.format(username = username, ip_address = ip_address, command = command)
			
			status = os.popen(cmd).read().split('\n')
			
			cpu_rate, memory_usage, total_time, cpu_temp, null_ = status

			cpu_rate = str("%.2f" % float(cpu_rate))
			memory_usage = str("%.2f" % float(memory_usage))
			total_time = str("%d" % float(total_time))
			cpu_temp = str("%d" % float(cpu_temp))

			print cpu_rate
			print memory_usage
			print total_time
			print cpu_temp

			Display.info_(screen, 'slave4', cpu_rate, memory_usage, total_time, cpu_temp)

		else:
			Display.connect_failure_(screen, 'slave4')
			
		screen.update()
		screen.disconnect()

	except Exception, e:
		print e	

if __name__ == '__main__':
	main()

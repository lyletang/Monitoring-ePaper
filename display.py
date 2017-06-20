#!/usr/bin/env python
# coding: utf-8
#Author: Jiahui Tang
#Date: 2017-06-20

#import the necessary packages
import datetime
from ePaper import *

#the main class
class Display(object):
	def __init__(self):
		pass

	def __str__(self):
		return "4.3inch-ePaper display"

	__repr__ = __str__

	@classmethod
	def time_(cls, screen):
		clock_x = 40
		clock_y = 0
		temp_x = 0
		temp_y = 0
		time_now = datetime.datetime.now()
		time_string = time_now.strftime('%H:%M')
		date_string = time_now.strftime('%Y-%m-%d')
		week_string = [u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日'][time_now.isoweekday() - 1]
		if time_string[0] == '0':
			time_string = time_string[1:]
			temp_x += 40

		for c in time_string:
			bmp_name = 'NUM{}.BMP'.format('S' if c == ':' else c)
			screen.bitmap(clock_x + temp_x, clock_y, bmp_name)
			temp_x += 70 if c == ':' else 100

		screen.set_ch_font_size(FONT_SIZE_48)
		screen.set_en_font_size(FONT_SIZE_48)
		
		#test print
		print date_string
		print week_string
		
		screen.text(clock_x + 350 + 140, clock_y + 10, date_string)
		screen.text(clock_x + 350 + 170, clock_y + 70, week_string)

	@classmethod
	def logo_(cls, screen):
		bmp_name = 'SPARK.BMP'
		screen.bitmap(20, 0 + 240, bmp_name)

		bmp_name = 'PI.BMP'
		screen.bitmap(20, 0 + 240 + 160, bmp_name)

	@classmethod
	def node_name_(cls,screen):
		screen.set_ch_font_size(FONT_SIZE_64)
		screen.set_en_font_size(FONT_SIZE_64)
		
		screen.text(200, 0 + 170, u'master')
		screen.text(200, 0 + 170 + 80, u'slave1')
		screen.text(200, 0 + 170 + 160, u'slave2')
		screen.text(200, 0 + 170 + 240, u'slave3')
		screen.text(200, 0 + 170 + 320, u'slave4')

	@classmethod
	def connect_failure_(cls, screen, *argv):
		bmp_name = 'NO.BMP'

		screen.set_ch_font_size(FONT_SIZE_48)
		screen.set_en_font_size(FONT_SIZE_48)
	
		if argv:
			if len(argv) == 1:
				if argv[0] == 'master':
					screen.bitmap(400, 0 + 170, bmp_name)	
					screen.text(400 + 80, 0 + 170, u'Connect fauilure! Please check!')
			
				elif argv[0] == 'slave1':
					screen.bitmap(400, 0 + 250, bmp_name)	
					screen.text(400 + 80, 0 + 250, u'Connect fauilure! Please check!')
		
				elif argv[0] == 'slave2':
					screen.bitmap(400, 0 + 330, bmp_name)	
					screen.text(400 + 80, 0 + 330, u'Connect fauilure! Please check!')
		
				elif argv[0] == 'slave3':
					screen.bitmap(400, 0 + 410, bmp_name)	
					screen.text(400 + 80, 0 + 410, u'Connect fauilure! Please check!')
		
				elif argv[0] == 'slave4':
					screen.bitmap(400, 0 + 490, bmp_name)	
					screen.text(400 + 80, 0 + 490, u'Connect fauilure! Please check!')
				
				else:
					raise ValueError		

			else:
				raise TypeError

		else:
			raise EOFError			
	

	@classmethod
	def info_(cls, screen, *argv):
		screen.set_ch_font_size(FONT_SIZE_32)
		screen.set_en_font_size(FONT_SIZE_32)
	
		print argv

		if argv:
			if argv[0] == 'master':
				print 'yes'
				screen.text(400, 0 + 170, u'CPU: {cpu_rate}'.format(cpu_rate = argv[1]))
				print '11111'
				screen.text(600, 0 + 170, u'RAM: {memory_usage}'.format(memory_usage = argv[2]))
				print '22222'				
				screen.text(400, 0 + 170 + 40, u'Uptime: {total_time}'.format(total_time = argv[3]))
				print '33333'
				screen.text(600, 0 + 170 + 40, u'CPUTemp: {cpu_temp}'.format(cpu_temp = argv[4]))	
				print 'nonno'		
	
			elif argv[0] == 'slave1':
				screen.text(400, 0 + 250, u'CPU: {cpu_rate}'.format(cpu_rate = argv[1]))
				screen.text(600, 0 + 250, u'RAM: {memory_usage}'.format(memory_usage = argv[2]))
				screen.text(400, 0 + 250 + 40, u'Uptime: {total_time}'.format(total_time = argv[3]))
				screen.text(600, 0 + 250 + 40, u'CPUTemp: {cpu_temp}'.format(cpu_temp = argv[4]))	
			elif argv[0] == 'slave2':
				screen.text(400, 0 + 330, u'CPU: {cpu_rate}'.format(cpu_rate = argv[1]))
				screen.text(600, 0 + 330, u'RAM: {memory_usage}'.format(memory_usage = argv[2]))
				screen.text(400, 0 + 330 + 40, u'Uptime: {total_time}'.format(total_time = argv[3]))
				screen.text(600, 0 + 330 + 40, u'CPUTemp: {cpu_temp}'.format(cpu_temp = argv[4]))
	
			elif argv[0] == 'slave3':
				screen.text(400, 0 + 410, u'CPU: {cpu_rate}'.format(cpu_rate = argv[1]))
				screen.text(600, 0 + 410, u'RAM: {memory_usage}'.format(memory_usage = argv[2]))
				screen.text(400, 0 + 410 + 40, u'Uptime: {total_time}'.format(total_time = argv[3]))
				screen.text(600, 0 + 410 + 40, u'CPUTemp: {cpu_temp}'.format(cpu_temp = argv[4]))
		
			elif argv[0] == 'slave4':
				screen.text(400, 0 + 490, u'CPU: {cpu_rate}'.format(cpu_rate = argv[1]))
				screen.text(600, 0 + 490, u'RAM: {memory_usage}'.format(memory_usage = argv[2]))
				screen.text(400, 0 + 490 + 40, u'Uptime: {total_time}'.format(total_time = argv[3]))
				screen.text(600, 0 + 490 + 40, u'CPUTemp: {cpu_temp}'.format(cpu_temp = argv[4]))	
			else:
				raise ValueError		

		else:
			print argv, len(argv)
			raise EOFError	

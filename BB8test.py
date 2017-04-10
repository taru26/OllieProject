#!/usr/bin/python
from bluepy import btle
import struct
import time
import BB8_driver
import sys
#import ViconTrackerPoseHandler

def move_to_dest(bb8, a, x, y):
"""
Function tomove bot to a particular destination

Parameters: 
	BB8_driver Object
	ViconTrackerPoseHandler object
	x coordinate of the bot
	y coordinate of the bot
"""
	while 1:
		
		
		print a.getPose()
		curr_x = a[0]
		curr_y = a[1]
		if curr_x==x and curr_y==y:
			break;
		# calculate heading angle
		angle = atan2((y-curr_y)/(x-curr_x)) # -pi to pi
		heading = degree(angle)
		bb8.roll(60, heading, 1, False)

'''
1. Create an object of ollie driver
2. Coonect to the bot
'''
bb8 = BB8_driver.Sphero()
bb8.connect()

bb8.start()
bb8.join()

'''If unable to connect to the bot'''
if False:
    print "Could not connect"
    

print "Starting to blink"
#time.sleep(.2)
bb8.set_rgb_led(255,0,0,0,False)
time.sleep(2)

'''Code for moving the bot to a particular position using vicon tracker'''
"""
print "Start moving"
a = ViconTrackerPoseHandler(None, None, "",51001, "Ollie_2")
move_to_dest(bb8, a, 0, 4)
"""

'''Move forward'''
bb8.roll(60, 0, 1, False)
time.sleep(2)
bb8.roll(0, 0, 1, False)

'''Move right'''
bb8.roll(60, 90, 1, False)
time.sleep(2)
bb8.roll(0, 90, 1, False)

'''Move backward'''
bb8.roll(60, 180, 1, False)
time.sleep(2)
bb8.roll(0, 180, 1, False)

'''Move left'''
bb8.roll(60, 270, 1, False)
time.sleep(2)
bb8.roll(0, 0, 1, False) # remove this


"""bb8.roll(65, 0, 1, False)
time.sleep(2)
bb8.roll(65, 90, 1, False)
time.sleep(2)
bb8.roll(65, 180, 1, False)
time.sleep(2)
bb8.roll(65, 270, 1, False)
time.sleep(2)"""

print "Stops motions"
#bb8.roll(10, 90, 1, False)

time.sleep(0.5)

'''Disconnect from the bot'''
bb8.disconnect()

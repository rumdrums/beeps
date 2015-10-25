#!/usr/bin/python

import os
import math
import sys
import time

magic=1.059463
tonic=220
length=200


def play_mode(mode):
	# modes defined lamely:
	if mode in 'ionian':
		interval = (2, 2, 1, 2, 2, 2, 1)
	elif mode in 'dorian':
		interval = (2, 1, 2, 2, 2, 1, 2)
	elif mode in 'phrygian': 
		interval = (1, 2, 2, 2, 1, 2, 2)
	elif mode in 'lydian':
		interval = (2, 2, 2, 1, 2, 2, 1)
	elif mode in 'mixolydian':
		interval = (2, 2, 1, 2, 2, 1, 2)
	elif mode in 'aeolian':
		interval = (2, 1, 2, 2, 1, 2, 2)
	elif mode in 'locrian':
		interval = (1, 2, 2, 1, 2, 2, 2)
	else:
		print("Fucked!")
		sys.exit()
	
	# play first pitch:
	pitch = tonic
	os.system("beep -f "+str(pitch)+"-l "+str(length))

	# then play subsequent intervals:
	for i in interval:
		pitch = pitch * (magic ** i);
		os.system("beep -f "+str(pitch)+"-l "+str(length))

for i in ['ionian','dorian','phrygian','lydian','mixolydian','aeolian','locrian']:
	print(i)
	play_mode(i)
	time.sleep(1)


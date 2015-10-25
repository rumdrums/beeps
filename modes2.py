#!/usr/bin/python

import os
import math
import sys
import time
import itertools

magic=1.059463
tonic=220
length=200
max_pitch=2000
modes=('ionian','dorian','phrygian','lydian','mixolydian','aeolian','locrian')

def play_mode(mode):
	# modes defined lamely:
	if mode in ['ionian', 1]:
		interval = (2, 2, 1, 2, 2, 2, 1)
	elif mode in ['dorian', 2]:
		interval = (2, 1, 2, 2, 2, 1, 2)
	elif mode in ['phrygian', 3]: 
		interval = (1, 2, 2, 2, 1, 2, 2)
	elif mode in ['lydian', 4]:
		interval = (2, 2, 2, 1, 2, 2, 1)
	elif mode in ['mixolydian', 5]:
		interval = (2, 2, 1, 2, 2, 1, 2)
	elif mode in ['aeolian', 6]:
		interval = (2, 1, 2, 2, 1, 2, 2)
	elif mode in ['locrian', 7]:
		interval = (1, 2, 2, 1, 2, 2, 2)
	else:
		print("Fucked!")
		sys.exit()

	
	# play first pitch:
	pitch = tonic
	os.system("beep -f "+str(pitch)+"-l "+str(length))

	cycle=itertools.cycle(interval)
	# then play subsequent intervals:
	i=1
	while i < 15:
		next=cycle.next()
		pitch = pitch * (magic ** next);
		os.system("beep -f "+str(pitch)+"-l "+str(length))
		i = i + 1

for i in modes:
	print(i)
	play_mode(i)
	time.sleep(1)


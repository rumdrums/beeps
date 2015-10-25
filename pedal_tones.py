#!/usr/bin/python

import os
import math
import sys
import time
import itertools

magic=1.059463
tonic=220
length=1
max_pitch=2000

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

	cycle=itertools.cycle(interval)
	# then play subsequent intervals:
	i=1
	while i < 15:
		next=cycle.next()
		pitch = pitch * (magic ** next);
		os.system("beep -f "+str(tonic)+"-l "+str(length))
		os.system("beep -f "+str(pitch)+"-l "+str(length))
		i = i + 1

for i in ['ionian','dorian','phrygian','lydian','mixolydian','aeolian','locrian']:
	print(i)
	play_mode(i)
	time.sleep(1)

#pitch = pitch * magic ** interval[i];

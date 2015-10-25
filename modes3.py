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

"""
1) Get interval pattern, ie mode
2) Create final pattern, including multiple iterations, etc.
3) Generate frequencies based on 2)
4) Pass frequencies (and time for each freq?) to function that plays them
"""

def get_mode(mode):
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

	return interval

def get_pitches(tonic, intervals):
	pitches = []	
	# start with tonic:
	pitches.append(tonic)
	
	# a quick way to have it play 2 octaves (multiply intervals by 2:):
	for i in intervals*2:
		pitch = pitches[-1] * (magic ** i);
		pitches.append(pitch)		
	
	return pitches

# this could easily be modified to take key:value with lengths that vary by note:
def play_pitches(pitches, length):
	for pitch in pitches: 
		os.system("beep -f "+str(pitch)+"-l "+str(length))

# for now, just play all modes:
for i in modes:
	print(i)
	mode=get_mode(i)
	pitches=get_pitches(tonic ,mode)
	play_pitches(pitches, length)
	time.sleep(1)

#cycle=itertools.cycle(interval)
	#i=1
	#while i < 15:
		#next=cycle.next()
		#os.system("beep -f "+str(pitch)+"-l "+str(length))
		#i = i + 1


#!/usr/bin/python

import os
import math

magic=1.059463
tonic=220
semi=tonic*magic
limit=800
length=200
fifth=tonic
tone=tonic

def semi(tone):
	return (tone*magic)

def whole(tone):
	return semi(tone*magic)	

def major():
	pitch = tonic
	intervals = [0, 2, 2, 1, 2, 2, 2, 1]
	for interval in intervals:
		pitch = pitch * magic ** interval;
		print(pitch)
		os.system("beep -f "+str(pitch)+"-l "+str(length))

major()

#OLD:
#while tone < limit:
	#fifth=(tonic*magic*magic*magic*magic*magic*magic)
	#os.system("beep -f "+str(tonic)+" -l "+str(length))
	#os.system("beep -f "+str(fifth)+" -l "+str(length))
	#tonic = (tonic*magic)



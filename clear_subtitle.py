from profanity import *
import time

def clean():

	profanity_purifier = PurifyText()

	f = open("./video/gordon.srt","r")
	k = f.readlines()
	full = "".join(k)
	print(full)
	f.close()

	clean = profanity_purifier.replace(full) 
	
	print("Detected Strong Language instances", clean['found'])

	print("")
	print("CLEANING")
	
	time.sleep(3)
	

	print(clean['text'])
	n = open("./video/gordon_clean.srt", "w+")
	n.write(clean['text'])

	n.close()
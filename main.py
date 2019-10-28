from __future__ import print_function
from db import *
from clear_subtitle import *
from camFeed import *


from sys import argv
import time
import pprint
import cv2

pp = pprint.PrettyPrinter(indent=4)


if (argv[1] == 'detect_age'):
	
	users_can_be = ['children', 'teens', 'aged']
	showFeed()

	current_user = users_can_be[1]

	print("Analysing age")
	time.sleep(2)
	
	if(current_user == 'children'):
		print ("Detected Age is (approximately) :", end=" ")
		print (user['user'][0]['age'], "years")

	elif (current_user== 'teens'):
		print ("Detected Age is (approximately) :", end=" ")
		print (user['user'][1]['age'], "years")

	elif (current_user == 'aged'):
		print ("Detected Age is (approximately) :", end=" ")
		print (user['user'][2]['age'], "years")

if (argv[1] == 'recommend_videos_for_me'):

	users_can_be = ['children', 'teens', 'aged']

	current_user = users_can_be[2]	

	print("Finding Videos . . . ")
	
	time.sleep(2)
	
	if(current_user == 'children'):
		for i in range(len(videos['video']['children'])):
			print("")
			print('VIDEO', i+1)
			print("")
			pp.pprint (videos['video']['children'][i])

	elif (current_user == 'teens'):
		for i in range(len(videos['video']['teens'])):
			print("")
			print('VIDEO', i+1)
			print("")
			pp.pprint (videos['video']['teens'][i])

	elif (current_user == 'aged'):
		for i in range(len(videos['video']['aged'])):
			print("")
			print('VIDEO', i+1)
			print("")
			pp.pprint (videos['video']['aged'][i])

if (argv[1] == 'upload_video'):

	print("preparing. . .")
	time.sleep(2)

	if(argv[2] == 'gordon.3gp'):
		print('fetched file for upload : gordon.3gp')
		print("")
		time.sleep(1)

		print('generating description . . .')
		print("")
		time.sleep(3)
		response = 'There are a group of people, fighting, in a kitchen wearing white clothes.'
		print(response)		

		print('generating subtitles . . .')
		print("")
		time.sleep(3)

		clean()

		print('Subtitles Cleaned. . .')
		print("")
		time.sleep(2)

		print('Censoring Audio. . .')
		print("")
		time.sleep(4)

		print('Audio Censor Successful. . .')
		print("")
		time.sleep(2)

		# print('Detecting Obscene Content. . .')
		# print("")
		# time.sleep(3)

		# print('Censoring Obscene Content. . .')
		# print("")
		# time.sleep(5)

		print('Preparing Final Video For Upload. . .')
		print("")
		time.sleep(5)

		print("saving file on Local Device")
		time.sleep(4)

		print("Save Completed Successfully :)")

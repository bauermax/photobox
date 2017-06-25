#imports for camera
from PIL import Image
from time import sleep
from time import gmtime, strftime
from picamera import *
import RPi.GPIO as GPIO

#IMPORTS FOR UPLOAD
import threading
import time

#IMPORT CONFIG
import yaml

#IMPORT EXTERNAL SCRIPTS
import processing

############################################################

#OPEN CONF YAML
fileconf = open('config.yaml', 'r')
conf = yaml.load(fileconf)


########## -CONST- ##########
#CAMERA
TAB_EFFECT = ['none','pastel','negative','sketch','oilpaint','cartoon','gpen','posterise','hatch','watercolor']
BUTTON_MAIN = conf['gpio']['main']
BUTTON_PREV = conf['gpio']['prev']
BUTTON_NEXT = conf['gpio']['next']

#SAVE
SAVE_FOLDER = conf['path']['images_folder']

CAMERA_WIDTH =  conf["camera"]["width"]
CAMERA_HEIGHT =  conf["camera"]["height"]


mB = 0 #MAIN BUTTON
nB = 0 #NEXT BUTTON
pB = 0 #PREVIOUS BUTTON

#VARIABLES
currentEffect = 0


GPIO.setmode(GPIO.BCM)
#MAIN BUTTON
GPIO.setup(BUTTON_MAIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#PREV BUTTON
GPIO.setup(BUTTON_PREV, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#NEXT BUTTON
GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
############################################################
#CORE FUNCTIONS
def changeFilter() :
	global currentEffect
	global TAB_EFFECT
	camera.image_effect = TAB_EFFECT[currentEffect % len(TAB_EFFECT)]

##########
def checkNext():
	global currentEffect
	global nB
	btState = GPIO.input(BUTTON_NEXT)

	if btState == 1 and nB == 0 :
		currentEffect += 1
		nB = 1
		changeFilter()
	elif btState == 0 and nB == 1:
		nB = 0
##########
def checkPrevious():

	global currentEffect
	global pB
	btState = GPIO.input(BUTTON_PREV)

	if btState == 1 and pB == 0 :
		currentEffect -= 1
		pB = 1
		changeFilter()
	elif btState == 0 and pB == 1:
		pB = 0
##########
def checkMain(picam):

	global currentEffect
	global mB
	btState = GPIO.input(BUTTON_MAIN)

	#IF PRESS PHOTO BUTTON
	if btState == 1 and mB == 0 :

		camera.annotate_text = " \n \n \n Souriez !!!"

		sleep(1)
		camera.annotate_text = " \n \n \n 3"
		sleep(0.5)
		camera.annotate_text = " \n \n \n 2"
		sleep(0.5)
		camera.annotate_text = " \n \n \n 1"
		sleep(0.5)
		camera.annotate_text = ""


		fname = SAVE_FOLDER +strftime("%Y_%m_%d_%H%M%S",gmtime())+'.jpg'
		#CAPTURE PHOTO
		picam.capture(fname)


		#START A THREAD WITH IMAGE PROCESSING + UPLOAD
		t = threading.Thread(target=processing.asyncTask, args=[fname])
		t.daemon = True
		t.start()



	elif btState == 0 and mB == 1:
		mB = 0


########## -MAIN- ##########
#CHECK IF OLD PROCESSED IMAGES ARE NOT UPLOADED --> THREAD
resume = threading.Thread(target=processing.resume_uploads, args=[])
resume.daemon = True
resume.start()
#CAMERA INIT
camera = PiCamera()
camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)
#FONT SIZE
camera.annotate_text_size = 130
#START DISPLAYING PREVIEW
camera.start_preview(resolution = (CAMERA_WIDTH, CAMERA_HEIGHT))
#START CAMERA WITH NO EFFECTS
camera.image_effect = 'none'

#MAIN LOOP
while 1:

	#CHECK IS A BUTTON IS PRESSED
	checkPrevious()
	checkNext()
	checkMain(camera)
	sleep(0.05)

#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# app.py
#######

from flask import Flask, render_template, request, redirect, url_for, make_response
import pwmmotors as motors
import json
import imagecapture as imagecapture

app = Flask(__name__) #set up flask server

#when the root IP is selected, return index.html page
@app.route('/')
def index():

	return render_template('index.html')

#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
		motors.turnLeft()
	elif changePin == 2:
		motors.forward()
	elif changePin == 3:
		motors.turnRight()
	elif changePin == 4:
		motors.backward()
	else:
		motors.stop()


	response = make_response(redirect(url_for('index')))
	return(response)

@app.route('/go/<direction>/<duration>', methods=['POST'])
def goRoute(direction, duration):
	print("goRoute" + direction + duration)
	duration = float(duration)
	
	if direction == "f":
		motors.forwardForXSeconds(duration)
	elif direction == "b":
		motors.backwardForXSeconds(duration)
	elif direction == "l":
		motors.turnLeftForXSeconds(duration)
	elif direction == "r":
		motors.turnRightForXSeconds(duration)
	elif direction == "s":
		motors.stop()

	return "success"

@app.route('/goTank/<leftOrRight>/<direction>/<duration>', methods=['POST'])
def goTankRoute(leftOrRight, direction, duration):
	print("goRoute" + direction + duration)
	duration = float(duration)
	
	
	if leftOrRight == "l":
		if direction == "f":
			motors.leftMotorForwardForXSeconds(duration)
		elif direction == "b":
			motors.leftMotorBackwardForXSeconds(duration)
		else:
			motors.leftStop()
	if leftOrRight == "r":
		if direction == "f":
			motors.rightMotorForwardForXSeconds(duration)
		elif direction == "b":
			motors.rightMotorBackwardForXSeconds(duration)
		else:
			motors.rightStop()

	return "success"

@app.route('/pickup', methods=['GET'])
def pickup():
	print("pickup")
	imgFile = imagecapture.captureImage()

	return imgFile

app.run(debug=False, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000

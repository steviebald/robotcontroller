# CamJam EduKit 3 - Robotics

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# How many times to turn the pin on and off each second
Frequency = 50
# How long the pin stays on each cycle, as a percen
ADutyCycle = 100 #Left motor
BDutyCycle = 100 #Right motor

# Settng the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
def stop():
    print("stop")
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def forward():
    print("forward")
    forwardForXSeconds(0)

# Turn both motors forwards for duration in seconds. If duration is 0 don't stop
def forwardForXSeconds(duration):
    print("pwm forward for " + str(duration))
    pwmMotorAForwards.ChangeDutyCycle(ADutyCycle)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(BDutyCycle)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

    if duration > 0:
    	time.sleep(duration)
    	stop()

# Turn both motors backwards
def backward():
    print("backward")
    backwardForXSeconds(0)

# Turn both motors backwards
def backwardForXSeconds(duration):
    print("pwm backward for " + str(duration))

    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(ADutyCycle)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(BDutyCycle)

    if duration > 0:
        time.sleep(duration)
        stop()

# Turn left
def turnLeft():
    print("turn left")
    turnLeftXSeconds(0)

def turnLeftForXSeconds(duration):
    print("pwm left for " + str(duration))

    pwmMotorAForwards.ChangeDutyCycle(ADutyCycle)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(BDutyCycle)

    if duration > 0:
        time.sleep(duration)
        stop()

# Turn Right
def turnRight():
    print("turn right")
    turnRightForXSeconds(0)

def turnRightForXSeconds(duration):
    print("pwm right for " + str(duration))

    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(ADutyCycle)
    pwmMotorBForwards.ChangeDutyCycle(BDutyCycle)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

    if duration > 0:
        time.sleep(duration)
        stop()

#These methods are for tank style control
def rightMotorForwardForXSeconds(duration):
    print("right forward for " + str(duration))
    pwmMotorAForwards.ChangeDutyCycle(ADutyCycle)
    pwmMotorABackwards.ChangeDutyCycle(Stop)

    if duration > 0:
    	time.sleep(duration)
    	pwmMotorAForwards.ChangeDutyCycle(Stop)

def rightMotorBackwardForXSeconds(duration):
    print("right backward for " + str(duration))
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(ADutyCycle)

    if duration > 0:
    	time.sleep(duration)
    	pwmMotorABackwards.ChangeDutyCycle(Stop)

def leftMotorForwardForXSeconds(duration):
    print("left forward for " + str(duration))
    pwmMotorBForwards.ChangeDutyCycle(ADutyCycle)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

    if duration > 0:
    	time.sleep(duration)
    	pwmMotorBForwards.ChangeDutyCycle(Stop)

def leftMotorBackwardForXSeconds(duration):
    print("left backward for " + str(duration))
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(ADutyCycle)

    if duration > 0:
    	time.sleep(duration)
    	pwmMotorBBackwards.ChangeDutyCycle(Stop)

def rightStop():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)

def leftStop():
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

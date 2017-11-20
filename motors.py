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

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)


# Turn all motors off
def stop():
    print("stop")
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)


# Turn both motors forwards
def forward():
    print("forward")
    forwardForXSeconds(0)

# Turn both motors forwards for duration in seconds. If duration is 0 don't stop
def forwardForXSeconds(duration):
    print("forward for " + str(duration))
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

    if duration > 0:
    	time.sleep(duration)
    	stop()

# Turn both motors backwards
def backward():
    print("backward for " + str(duration))
    backwardForXSeconds(0)

# Turn both motors backwards
def backwardForXSeconds(duration):
    print("backward for " + str(duration))

    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

    if duration > 0:
        time.sleep(duration)
        stop()

# Turn left
def turnLeft():
    print("turn left")
    turnLeftXSeconds(0)

def turnLeftForXSeconds(duration):
    print("left for " + str(duration))

    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

    if duration > 0:
        time.sleep(duration)
        stop()

# Turn Right
def turnRight():
    print("turn right")
    turnRightForXSeconds(0)

def turnRightForXSeconds(duration):
    print("right for " + str(duration))

    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

    if duration > 0:
        time.sleep(duration)
        stop()


#stop motors at start
stop()


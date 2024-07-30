import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()



Forward=12,13
Backward=11,15
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def reverse(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving reverse..")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def forward(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving forward..")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)


                               

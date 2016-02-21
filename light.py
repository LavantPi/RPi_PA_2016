import RPi.GPIO as GPIO
import time
import settings

def init(lightNo):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(lightNo,GPIO.OUT)
    switch(lightNo,GPIO.HIGH)
    time.sleep(0.3)
    switch(lightNo,GPIO.LOW)
    print "light on GPIO %d initialised" %lightNo

def switch(lightNo,state):
    "Turn the light on or off"
    print "turning on light on GPIO %d" %lightNo
    GPIO.output(lightNo,state)
    
    

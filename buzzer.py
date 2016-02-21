import RPi.GPIO as GPIO
import time

def init(buzzerNo):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzerNo,GPIO.OUT)
    buzz(buzzerNo,GPIO.HIGH)
    time.sleep(0.5)
    buzz(buzzerNo,GPIO.LOW)
    print "buzzer on GPIO %d initialised" %buzzerNo

def buzz(buzzerNo,state):
    "Turn the buzzer on or off"
    GPIO.output(buzzerNo,state)
    
    

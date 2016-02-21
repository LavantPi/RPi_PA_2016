import RPi.GPIO as GPIO

def init(buttonNo):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonNo,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    print "button on GPIO %d initialised" %buttonNo

def isPressed(buttonNo):
    "Checks if button is pressed"
    pressed = False
    inputState = GPIO.input(buttonNo)
#    print "button is %d" %inputState
    if inputState == False:
        pressed = True
    return pressed

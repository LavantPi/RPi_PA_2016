import RPi.GPIO as GPIO

def init(switchNo):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switchNo,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    print "switch on GPIO %d initialised" %switchNo

def gameSwitch(switchOne,switchTwo):
    inputState1 = GPIO.input(switchOne)
    inputState2 = GPIO.input(switchTwo)
    gameNo = 1
    print "input state1 is %d" %inputState1
    print "input state2 is %d" %inputState2
    if inputState2 == False:
        gameNo = 2
    print "game is %d" %gameNo
    
    return gameNo

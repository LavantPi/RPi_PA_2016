import button
import light
import buzzer
import switch
import RPi.GPIO as GPIO

def init():
    "Initializes the global variables"
    GPIO.cleanup()

    #definition of the switches
    global switch1
    switch1 = 19
    global switch2
    switch2 = 26
    switch.init(switch1)
    switch.init(switch2)
    
    #definition of the buttons
    global button1
    button1 = 2
    global button2
    button2 = 3
    global button3
    button3 = 4
    global button4
    button4 = 17
    global button5
    button5 = 27
    global button6
    button6 = 22
    global startButton
    startButton = 6
    #List of the buttons
    global buttonList
    buttonList = [button1,button2,button3,button4,button5,button6]

    button.init(startButton)
    for buttonNo in buttonList:
        button.init(buttonNo)

    # definition of the lights
    global light1
    light1 = 20
    global light2
    light2 = 21
    global light3
    light3 = 18
    global light4
    light4 = 23
    global light5
    light5 = 24
    global light6
    light6 = 10
    global readylight
    readylight = 13
    #List of the lights
    global lightList
    lightList = [light1,light2,light3,light4,light5,light6]

    for lightNo in lightList:
        light.init(lightNo)

    light.init(readylight)
    
    #definition of the buzzers
    global buzzer1
    buzzer1 = 9
    global buzzer2
    buzzer2 = 25
    global buzzer3
    buzzer3 = 11
    global buzzer4
    buzzer4 = 8
    global buzzer5
    buzzer5 = 7
    global buzzer6
    buzzer6 = 5
    #List of the buzzers
    global buzzerList
    buzzerList = [buzzer1,buzzer2,buzzer3,buzzer4,buzzer5,buzzer6]

    for buzzerNo in buzzerList:
        buzzer.init(buzzerNo)

    

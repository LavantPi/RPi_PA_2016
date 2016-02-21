import time
import button
import settings
import random
import light
import buzzer
import switch 
import RPi.GPIO as GPIO

#turn off all lights and buzzers
settings.init()
nextNumber = -1
BUZZ_TIME = 5
GAME_TIME = 10
game = 2

testNo = 0
while testNo < 6:
    testDone = False
    light.switch(settings.lightList[testNo],GPIO.HIGH)
    while not testDone:
        testDone = button.isPressed(settings.buttonList[testNo])
    buzzer.buzz(settings.buzzerList[testNo],GPIO.HIGH)
    time.sleep(1)
    light.switch(settings.lightList[testNo],GPIO.LOW)
    buzzer.buzz(settings.buzzerList[testNo],GPIO.LOW)
    testNo = testNo + 1
                

while True:
    started = False
    light.switch(settings.readylight,GPIO.HIGH)
    while not started:
        started = button.isPressed(settings.startButton)
    light.switch(settings.readylight,GPIO.LOW)

    playing = True
    GAME_TIME = 10
    BUZZ_TIME = 5
    game = switch.gameSwitch(settings.switch1,settings.switch2)
    if game == 1:
        while playing:
            pressed = False
            startTime = time.time()
            nextNo = random.randint(0,5)
            GAME_TIME = GAME_TIME-0.2
            BUZZ_TIME = GAME_TIME/2
            light.switch(settings.lightList[nextNo],GPIO.HIGH)
            buzzer.buzz(settings.buzzerList[nextNo],GPIO.HIGH)

            while not pressed and playing:
                pressed = button.isPressed(settings.buttonList[nextNo])
                newTime = time.time()
                if newTime - startTime>BUZZ_TIME:
                    buzzer.buzz(settings.buzzerList[nextNo],GPIO.LOW)
                if pressed == True:
                    light.switch(settings.lightList[nextNo],GPIO.LOW)
                    buzzer.buzz(settings.buzzerList[nextNo],GPIO.LOW)
                if newTime-startTime>GAME_TIME:
                    playing = False
                    light.switch(settings.lightList[nextNo],GPIO.LOW)
                    buzzer.buzz(settings.buzzerList[nextNo],GPIO.LOW)

            
            
    elif game == 2:
        while playing:
            pressed = False
            startTime = time.time()
            nextNo1 = random.randint(0,5)
            nextNo2 = random.randint(0,5)
            while nextNo2 == nextNo1:
                nextNo2 = random.randint(0,5)
            GAME_TIME = GAME_TIME-0.2
            BUZZ_TIME = GAME_TIME/2
            light.switch(settings.lightList[nextNo1],GPIO.HIGH)
            buzzer.buzz(settings.buzzerList[nextNo1],GPIO.HIGH)
            light.switch(settings.lightList[nextNo2],GPIO.HIGH)
            buzzer.buzz(settings.buzzerList[nextNo2],GPIO.HIGH)
            while not pressed and playing:
                pressed = button.isPressed(settings.buttonList[nextNo1])
                pressed = pressed and button.isPressed(settings.buttonList[nextNo2])
                newTime = time.time()
                if newTime - startTime>BUZZ_TIME:
                    buzzer.buzz(settings.buzzerList[nextNo1],GPIO.LOW)
                    buzzer.buzz(settings.buzzerList[nextNo2],GPIO.LOW)
                if pressed == True:
                    light.switch(settings.lightList[nextNo1],GPIO.LOW)
                    buzzer.buzz(settings.buzzerList[nextNo1],GPIO.LOW)
                    light.switch(settings.lightList[nextNo2],GPIO.LOW)
                    buzzer.buzz(settings.buzzerList[nextNo2],GPIO.LOW)                
                if newTime-startTime>GAME_TIME:
                    playing = False
                    light.switch(settings.lightList[nextNo1],GPIO.LOW)
                    buzzer.buzz(settings.buzzerList[nextNo1],GPIO.LOW)
                    light.switch(settings.lightList[nextNo2],GPIO.LOW)
                    buzzer.buzz(settings.buzzerList[nextNo2],GPIO.LOW)



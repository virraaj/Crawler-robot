'''
____________________________________________________________________________
*** This file takes care of all the necessary pin settings. ***
* pinSetup() is a method that single handedly defines all the required input and
output pins of the RaspberryPi Zero board. *
* valueRead_ON() deals with defining the GPIO pins for ON/OFF switch. Also it
takes no input arguements and  returns the state of the switch. *
* valueRead_alg() deals with defining the GPIO pins for Algorithm selection
switch. Also it takes no input arguements and returns the state of the switch.*
* valueRead_dir() deals with defining the GPIO pins for Forward / Backward
switch. Also it takes no input arguements and returns the state of the switch.*
______________________________________________________________________________
'''

# ___________ impoering dependencies ___________ #

import RPi.GPIO as GPIO


# ___________ pinSetup definition ___________ #

def pinSetup():
    # motor setup
    servoPIN = 17
    servoPIN1 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    # p is handle name for all the operations related to first servo motor (for first arm)
    p = GPIO.PWM(servoPIN, 50)
    # p1 is handle name for all the operations related to second servo motor (for second arm)
    p1 = GPIO.PWM(servoPIN1, 50)

    # encoder setup
    import KY040.ky040.KY040_V2 as ky
    CLOCKPIN = 20
    DATAPIN = 26
    SWITCHPIN = 2

    def rotaryChange(direction):
        pass

    GPIO.setmode(GPIO.BCM)
    encoder = ky.KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange)  # defining object of class KY040
    encoder.start()
    ENClast = 0

    # return
    return [p, p1, encoder, ENClast]


# ___________ valueRead_ON definition ___________ #

def valueRead_ON():
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # OFF POSITION
    val1 = GPIO.input(12)
    return val1


# ___________ valueRead_alg definition ___________ #

def valueRead_alg():
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	 # Qlambda learning
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Q learning
    if GPIO.input(13):
        return "Qlambda Learning"
    elif GPIO.input(19):
        return "Q Learning"
    else:
        return "Value iteration"


# ___________ valueRead_dir definition ___________ #

def valueRead_dir():
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Backward
    if GPIO.input(6):
        return 2  # forward movement
    else:
        return 1  # backward movement

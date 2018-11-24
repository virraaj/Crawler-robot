import RPi.GPIO as GPIO
def pinSetup():
    # motor setup
    servoPIN = 17
    servoPIN1 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz
    p1 = GPIO.PWM(servoPIN1, 50)


    # encoder setup
    import KY040.ky040.KY040_V2 as ky
    from time import sleep

    CLOCKPIN = 20
    DATAPIN = 26
    SWITCHPIN = 2
    #i = 0

    def rotaryChange(direction):
        #  global i
        #    print i
        # i=i+1

        # print "turned - " + str(direction)
        # def switchPressed():
        #    print "button pressed"
        pass

    GPIO.setmode(GPIO.BCM)

    encoder = ky.KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange)

    encoder.start()

    # encoder = ky.KY040
    ENClast = 0

    # return
    return [p, p1, encoder, ENClast]

def valueRead_ON():
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # OFF POSITION
    val1 = GPIO.input(5)
#    print "val1=", val1
    return val1
#    if val1:
#	return "OFF"
#    else:
#	return "ON"

def valueRead_alg():
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	 # Qlambda learning
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Q learning
    if  GPIO.input(13):
	return "Qlambda Learning"
    elif GPIO.input(19):
	return "Q Learning"
    else:
	return "Value iteration"

def valueRead_dir():
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Backward
    if GPIO.input(6):
	return 2
    else:
	return 1


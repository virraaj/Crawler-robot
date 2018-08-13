
def pinSetup():
    # motor setup
    import RPi.GPIO as GPIO
    servoPIN = 17
    servoPIN1 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    GPIO.setup(servoPIN1, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz
    p1 = GPIO.PWM(servoPIN1, 50)
    p.start(2.5)
    p1.start(2.5)
    # encoder setup
    import KY040.ky040.KY040_V2 as ky
    from time import sleep
    if __name__ == "__main__":

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

        try:
            while True:
                sleep(0.1)
        finally:
            encoder.stop()
            GPIO.cleanup()
    # encoder = ky.KY040
    ENClast = 0

    # return
    return [p, p1, encoder, ENClast]

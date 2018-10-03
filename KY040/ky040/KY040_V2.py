import RPi.GPIO as GPIO
from time import sleep


class KY040:

    CLOCKWISE = 0
    ANTICLOCKWISE = 1

    def __init__(self, clockPin, dataPin, switchPin=None, rotaryCallback=None, switchCallback=None, rotaryBouncetime=250, switchBouncetime=300):
        # persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback
        self.rotaryBouncetime = rotaryBouncetime
        self.switchBouncetime = switchBouncetime

        # setup pins
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)

        if None != self.switchPin:
            GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING,
                              callback=self._clockCallback, bouncetime=self.rotaryBouncetime)

        if None != self.switchPin:
            GPIO.add_event_detect(self.switchPin, GPIO.FALLING,
                                  callback=self._switchCallback, bouncetime=self.switchBouncetime)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)

        if None != self.switchPin:
            GPIO.remove_event_detect(self.switchPin)

    def _clockCallback(self, pin):
        #global c
        #global ac

        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 1:

                self.rotaryCallback(self.ANTICLOCKWISE)
#                print 'ac=', self.CLOCKWISE
                self.CLOCKWISE -= 1
                #ac = ac+1
            else:
                #global c
                self.rotaryCallback(self.CLOCKWISE)
#                print 'c=', self.CLOCKWISE
                self.CLOCKWISE += 1

    def setData(self, value):
        self.CLOCKWISE = value

    def getData(self):
        return self.CLOCKWISE

    def _switchCallback(self, pin):
        if None == self.switchPin:
            return

        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()


'''
************************************************
trying to call the class from pinSetup
************************************************
if __name__ == "__main__":
    CLOCKPIN = 20
    DATAPIN = 26
    SWITCHPIN = 2
    #i = 0
    def rotaryChange(direction):
        #global i
        #print i
        # i=i+1
        #print "turned - " + str(direction)
        # def switchPressed():
        #    print "button pressed"
        pass
    GPIO.setmode(GPIO.BCM)
    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange)
    ky040.start()

    GPIO.setmode(GPIO.BCM)

    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange)

    ky040.start()

    try:
        while True:
            sleep(0.1)
    finally:
        ky040.stop()
        GPIO.cleanup()
'''

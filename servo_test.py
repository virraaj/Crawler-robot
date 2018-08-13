import RPi.GPIO as GPIO
import time

servoPIN = 17
servoPIN1 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN1, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 as PWM with 50Hz
p1 = GPIO.PWM(servoPIN1, 50)
n = 5 #number of positions
p.start(2.5) # Initialising left-right motor
p1.start(2.5) # Initialising up-down motor as motor2
def frange(start, end, step):
    tmp = start
    step = (end - start) / (n-1)
    for i in range(0, n):
        yield tmp
        tmp += step
def motor2(t): # positions for up-down motor
    for i in frange(10.0,3.0,n):

        p1.ChangeDutyCycle(i)
        time.sleep(t)
        '''p1.ChangeDutyCycle(7.5) #This are the positions tested
        time.sleep(t)
        p1.ChangeDutyCycle(5.0)
        time.sleep(t)
        p1.ChangeDutyCycle(3.0)
        time.sleep(t)'''

def fwd(t): # positions programmed to move crawler forward
    for i in frange(5.0,3.0,n):
        for j in frange(10.0,3.0,n):
            p.ChangeDutyCycle(i)
            time.sleep(t)
            p1.ChangeDutyCycle(j)
            time.sleep(t)

    '''p.ChangeDutyCycle(5.0) #This are the positions programmed
    time.sleep(t)
    p1.ChangeDutyCycle(10.0)
    time.sleep(t)
    p1.ChangeDutyCycle(7.5)
    time.sleep(t)
    p1.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(3.0)
    time.sleep(t)
    '''
def rev(t):   # Crawler programmed to reverse by this function
    p.ChangeDutyCycle(5)
    time.sleep(t)
    #p1.ChangeDutyCycle(10)
    #time.sleep(t)
    motor2(0.5)

try:
  while True:
    #rev(0.5)
    fwd(0.5)

except KeyboardInterrupt:
  p.stop()
  p1.stop()
  GPIO.cleanup()

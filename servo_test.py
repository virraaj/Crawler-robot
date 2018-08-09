import RPi.GPIO as GPIO
import time

servoPIN = 17
servoPIN1 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN1, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p1 = GPIO.PWM(servoPIN1, 50)
n = 5
p.start(2.5) # Initialisierung
p1.start(2.5)
def frange(start, end, step):
    tmp = start
    while(tmp >= end):
        yield tmp
        tmp -= step 
def motor2(t):
    for i in frange(10.0,3.0,(10.0 - 3.0)/(n-1)):

        p1.ChangeDutyCycle(i)
        time.sleep(t)
        '''p1.ChangeDutyCycle(7.5)
        time.sleep(t)
        p1.ChangeDutyCycle(5.0)
        time.sleep(t)
        p1.ChangeDutyCycle(3.0)
        time.sleep(t)'''

def fwd(t):
    for i in frange(5.0,3.0,(5-3.0)/(n-1)):
        for j in frange(10.0,3.0,(10-3.0)/(n-1)):
            p.ChangeDutyCycle(i)
            time.sleep(t)
            p1.ChangeDutyCycle(j)
            time.sleep(t)

    '''p.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(10.0)
    time.sleep(t)
    p1.ChangeDutyCycle(7.5)
    time.sleep(t)
    p1.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(3.0)
    time.sleep(t)
    p.ChangeDutyCycle(3.33)
    time.sleep(t)
    p1.ChangeDutyCycle(3.0)
    time.sleep(t)
    p1.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(7.5)
    time.sleep(t)
    p1.ChangeDutyCycle(10.0)
    time.sleep(t)'''
def rev(t):
    p.ChangeDutyCycle(5)
    time.sleep(t)
    #p1.ChangeDutyCycle(10)
    #time.sleep(t)
    motor2(0.5)

try:
  while True:
    #rev(0.5)
    fwd(0.5)
    '''p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    motor2(0.5)
    p.ChangeDutyCycle(3.33)
    time.sleep(0.5)
    motor2(0.5)'''
    #p.ChangeDutyCycle(5.0)
    #time.sleep(0.5)
    #motor2(0.5)
    #p.ChangeDutyCycle(4.16)
    #time.sleep(0.5)
    #motor2(0.5)
    '''p.ChangeDutyCycle(10.0)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5.0)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)'''
except KeyboardInterrupt:
  p.stop()
  p1.stop()
  GPIO.cleanup()

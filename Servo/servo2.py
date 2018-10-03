import RPi.GPIO as GPIO
import time
servoPIN1 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
p1 = GPIO.PWM(servoPIN1, 50)
p1.start(5.0)
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(5.0)
try:
  while True:
    p.ChangeDutyCycle(3.0/50*50)


    '''p1.ChangeDutyCycle(10.0)
    time.sleep(0.5)
    
    p1.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    
    p1.ChangeDutyCycle(5.0)
    time.sleep(0.5)'''
    
    p1.ChangeDutyCycle(3.0/50*50)
    #time.sleep(1)
    
except KeyboardInterrupt:
  
  p1.stop()
  GPIO.cleanup()


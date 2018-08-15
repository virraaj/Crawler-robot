import RPi.GPIO as GPIO
import time
servoPIN1 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
p1 = GPIO.PWM(servoPIN1, 50)
p1.start(2.5)
try:
  while True:
    p1.ChangeDutyCycle(3.0)
    time.sleep(0.5)
    
    '''p1.ChangeDutyCycle(3.33)
    time.sleep(0.5)
    
    p1.ChangeDutyCycle(4.16)
    time.sleep(0.5)
    
    p1.ChangeDutyCycle(5.0)
    time.sleep(0.5)'''
    
except KeyboardInterrupt:
  
  p1.stop()
  GPIO.cleanup()


import RPi.GPIO as GPIO
import time

servoPIN = 17
servoPIN1 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN1, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p1 = GPIO.PWM(servoPIN1, 50)
def motor2(t):
    p1.ChangeDutyCycle(8.0)
    time.sleep(t)
    p1.ChangeDutyCycle(7.5)
    time.sleep(t)
    p1.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(3.5)
    time.sleep(t)
p.start(2.5) # Initialisierung
p1.start(2.5)
def fwd(t):
    p.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(10.0)
    time.sleep(t)
    p1.ChangeDutyCycle(7.5)
    time.sleep(t)
    p1.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(3.0)
    time.sleep(t)
    p.ChangeDutyCycle(4.17)
    time.sleep(t)
    p1.ChangeDutyCycle(10.0)
    time.sleep(t)
    '''p1.ChangeDutyCycle(5.0)
    time.sleep(t)
    p1.ChangeDutyCycle(7.5)
    time.sleep(t)
    p1.ChangeDutyCycle(10.0)
    time.sleep(t)'''
def rev(t):
<<<<<<< HEAD
    p.ChangeDutyCycle(5.0)
    time.sleep(t)
    motor2(0.5)
=======
    #p.ChangeDutyCycle(5.0)
    #time.sleep(t)
    motor2(t) 
>>>>>>> 70701c3e05a4aa811dcb80be39662b466b682b07

try:
  while True:
    #fwd(0.5)
    rev(0.5)
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

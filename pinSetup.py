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
    import ky040.KY040
    encoder = ky040
    ENClast = 0

    # return
    return [p, p1, encoder, ENClast]

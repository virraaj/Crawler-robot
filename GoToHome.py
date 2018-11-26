import time
def GoToHome(p, p1):
    p.ChangeDutyCycle(3.0)
    p1.ChangeDutyCycle(8.5)
    time.sleep(0.1)

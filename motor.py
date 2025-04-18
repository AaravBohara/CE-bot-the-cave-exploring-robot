import RPi.GPIO as GPIO
from time import sleep

enb = 14
in3 = 15
in4 = 18

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(enb,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    
def loop():
    pwm.ChangeDutyCycle(100)
    GPIO.output(enb,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(5)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(5)
    GPIO.output(enb,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    sleep(5)
    
def destroy():
    GPIO.cleanup()
    
if __name__=='__main__':
    setup()
    pwm = GPIO.PWM(enb,800)
    pwm.start(0)
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        destroy()
    
    
    
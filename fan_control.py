from gpiozero import CPUTemperature
import RPi.GPIO as GPIO

cpu = CPUTemperature().temperature

Fan = 36
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup (Fan,GPIO.OUT)

while True:
    print(cpu)
    if(cpu > 45.0):
        GPIO.output(Fan,GPIO.HIGH)
    else:
        GPIO.output(Fan,GPIO.LOW)
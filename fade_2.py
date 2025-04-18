from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)
while True:
    led.value = 0							
    sleep(0.05)
    led.value = 0.1							
    sleep(0.05)
    led.value = 0.2							
    sleep(0.05)
    led.value = 0.3							
    sleep(0.05)
    led.value = 0.4							
    sleep(0.05)
    led.value = 0.5							
    sleep(0.05)
    led.value = 0.6							
    sleep(0.05)
    led.value = 0.7							
    sleep(0.05)
    led.value = 0.8							
    sleep(0.05)
    led.value = 0.9
    sleep(0.05)
    led.value = 1							
    sleep(0.05)
    led.value = 0.9							
    sleep(0.05)
    led.value = 0.8							
    sleep(0.05)
    led.value = 0.7							
    sleep(0.05)
    led.value = 0.6							
    sleep(0.05)
    led.value = 0.5							
    sleep(0.05)
    led.value = 0.4							
    sleep(0.05)
    led.value = 0.3							
    sleep(0.05)
    led.value = 0.2							
    sleep(0.05)
    led.value = 0.1							
    sleep(0.05)
    led.value = 0
    sleep(0.05)

from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)
while True:
    led.value = 0							#led is off
    sleep(1)
    led.value = 0.5							#led is on half brightness
    sleep(1)
    led.value = 1							#led is on full brightness
    sleep(1)

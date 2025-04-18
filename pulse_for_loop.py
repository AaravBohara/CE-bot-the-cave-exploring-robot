from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)
while True:
    for (i) in range (0,10,1):
        led.value = i/10
        sleep(0.05)
    for (j) in range (10,0,-1):
        led.value = j/10
        sleep(0.05)
     
from gpiozero import LED
from time import sleep

led = LED(17)

while True:                                     #while true=infinte loop
    led.on()
    sleep(0.05)
    led.off()
    sleep(0.05)
    
          
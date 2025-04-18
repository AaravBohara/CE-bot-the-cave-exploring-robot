from gpiozero import LED
from time import sleep

led_red = LED(17)
led_blue = LED(26)

while True:                                     #while true=infinte loop
    led_red.on()
    led_blue.off()
    sleep(1)
    led_red.off()
    led_blue.on()
    sleep(1)
    
          

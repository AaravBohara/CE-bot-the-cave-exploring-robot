from gpiozero import LED
from time import sleep
led_red = LED(17)
led_blue = LED(27)								#blue = green
led_yellow = LED(22)
while True:
    red_light = input("give a number for red_light duration:")
    blue_light = input("give a number for blue_light duration:")
    led_blue.on()
    sleep(float(blue_light))
    led_blue.off()
    led_yellow.on()
    sleep(5)
    led_yellow.off()
    led_red.on()
    sleep(float(red_light))
    led_red.off()


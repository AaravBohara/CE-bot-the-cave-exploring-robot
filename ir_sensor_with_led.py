import RPi.GPIO as IO
from gpiozero import LED 

back_ir = 20
led = LED(21)
IO.setmode(IO.BCM)
IO.setup(back_ir, IO.IN)

try:
    while True:
        print(IO.input(back_ir))
        if not (IO.input(back_ir)):
            led.on()
        else:
            led.off()
except KeyboardInterrupt:
    IO.cleanup()
import RPi.GPIO as IO
import time

back_ir = 20
IO.setmode(IO.BCM)
IO.setup(back_ir, IO.IN)

try:
    while True:
        print(IO.input(back_ir))
except KeyboardInterrupt:
    IO.cleanup()
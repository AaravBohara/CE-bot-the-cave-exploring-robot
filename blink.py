from gpiozero import LED
from signal import pause
led = LED (16)
led.blink()
pause()

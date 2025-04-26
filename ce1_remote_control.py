import RPi.GPIO as GPIO
from time import sleep
import curses

ena_l = 18
in1_l = 14
in2_l = 15
enb_l = 25
in3_l = 23
in4_l = 24
ena_r = 1
in1_r = 8
in2_r = 7
enb_r = 21
in3_r = 20
in4_r = 16
back_ir = 26
front_ir = 19
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ena_l,GPIO.OUT)
    GPIO.setup(in1_l,GPIO.OUT)
    GPIO.setup(in2_l,GPIO.OUT)
    GPIO.setup(enb_l,GPIO.OUT)
    GPIO.setup(in3_l,GPIO.OUT)
    GPIO.setup(in4_l,GPIO.OUT)
    GPIO.setup(ena_r,GPIO.OUT)
    GPIO.setup(in1_r,GPIO.OUT)
    GPIO.setup(in2_r,GPIO.OUT)
    GPIO.setup(enb_r,GPIO.OUT)
    GPIO.setup(in3_r,GPIO.OUT)
    GPIO.setup(in4_r,GPIO.OUT)
    GPIO.setup(front_ir,GPIO.IN)
    GPIO.setup(back_ir,GPIO.IN)
    
    
def forward():
    GPIO.output(ena_l,GPIO.HIGH)
    GPIO.output(enb_l,GPIO.HIGH)
    GPIO.output(ena_r,GPIO.HIGH)
    GPIO.output(enb_r,GPIO.HIGH)
    GPIO.output(in1_l,GPIO.HIGH)
    GPIO.output(in2_l,GPIO.LOW)
    GPIO.output(in3_l,GPIO.HIGH)
    GPIO.output(in4_l,GPIO.LOW)
    GPIO.output(in1_r,GPIO.HIGH)
    GPIO.output(in2_r,GPIO.LOW)
    GPIO.output(in3_r,GPIO.HIGH)
    GPIO.output(in4_r,GPIO.LOW)
    return

def reverse():
    GPIO.output(ena_l,GPIO.HIGH)
    GPIO.output(enb_l,GPIO.HIGH)
    GPIO.output(ena_r,GPIO.HIGH)
    GPIO.output(enb_r,GPIO.HIGH)
    GPIO.output(in1_l,GPIO.LOW)
    GPIO.output(in2_l,GPIO.HIGH)
    GPIO.output(in3_l,GPIO.LOW)
    GPIO.output(in4_l,GPIO.HIGH)
    GPIO.output(in1_r,GPIO.LOW)
    GPIO.output(in2_r,GPIO.HIGH)
    GPIO.output(in3_r,GPIO.LOW)
    GPIO.output(in4_r,GPIO.HIGH)
    return
    
def left():
    GPIO.output(ena_l,GPIO.LOW)
    GPIO.output(enb_l,GPIO.LOW)
    GPIO.output(ena_r,GPIO.HIGH)
    GPIO.output(enb_r,GPIO.HIGH)
    GPIO.output(in1_l,GPIO.LOW)
    GPIO.output(in2_l,GPIO.LOW)
    GPIO.output(in3_l,GPIO.LOW)
    GPIO.output(in4_l,GPIO.LOW)
    GPIO.output(in1_r,GPIO.HIGH)
    GPIO.output(in2_r,GPIO.LOW)
    GPIO.output(in3_r,GPIO.HIGH)
    GPIO.output(in4_r,GPIO.LOW)
    return

def right():
    GPIO.output(ena_l,GPIO.HIGH)
    GPIO.output(enb_l,GPIO.HIGH)
    GPIO.output(ena_r,GPIO.LOW)
    GPIO.output(enb_r,GPIO.LOW)
    GPIO.output(in1_l,GPIO.HIGH)
    GPIO.output(in2_l,GPIO.LOW)
    GPIO.output(in3_l,GPIO.HIGH)
    GPIO.output(in4_l,GPIO.LOW)
    GPIO.output(in1_r,GPIO.LOW)
    GPIO.output(in2_r,GPIO.LOW)
    GPIO.output(in3_r,GPIO.LOW)
    GPIO.output(in4_r,GPIO.LOW)
    return
    
def reverse_left():
    GPIO.output(ena_l,GPIO.LOW)
    GPIO.output(enb_l,GPIO.LOW)
    GPIO.output(ena_r,GPIO.HIGH)
    GPIO.output(enb_r,GPIO.HIGH)
    GPIO.output(in1_l,GPIO.LOW)
    GPIO.output(in2_l,GPIO.LOW)
    GPIO.output(in3_l,GPIO.LOW)
    GPIO.output(in4_l,GPIO.LOW)
    GPIO.output(in1_r,GPIO.LOW)
    GPIO.output(in2_r,GPIO.HIGH)
    GPIO.output(in3_r,GPIO.LOW)
    GPIO.output(in4_r,GPIO.HIGH)
    return

def reverse_right():
    GPIO.output(ena_l,GPIO.HIGH)
    GPIO.output(enb_l,GPIO.HIGH)
    GPIO.output(ena_r,GPIO.LOW)
    GPIO.output(enb_r,GPIO.LOW)
    GPIO.output(in1_l,GPIO.LOW)
    GPIO.output(in2_l,GPIO.HIGH)
    GPIO.output(in3_l,GPIO.LOW)
    GPIO.output(in4_l,GPIO.HIGH)
    GPIO.output(in1_r,GPIO.LOW)
    GPIO.output(in2_r,GPIO.LOW)
    GPIO.output(in3_r,GPIO.LOW)
    GPIO.output(in4_r,GPIO.LOW)
    return

def stop():
    GPIO.output(ena_l,GPIO.LOW)
    GPIO.output(enb_l,GPIO.LOW)
    GPIO.output(ena_r,GPIO.LOW)
    GPIO.output(enb_r,GPIO.LOW)
    GPIO.output(in1_l,GPIO.LOW)
    GPIO.output(in2_l,GPIO.LOW)
    GPIO.output(in3_l,GPIO.LOW)
    GPIO.output(in4_l,GPIO.LOW)
    GPIO.output(in1_r,GPIO.LOW)
    GPIO.output(in2_r,GPIO.LOW)
    GPIO.output(in3_r,GPIO.LOW)
    GPIO.output(in4_r,GPIO.LOW)
    return

def control():
    char = screen.getch()
    if char == curses.KEY_UP:
        forward()
    elif char == curses.KEY_DOWN:
        reverse()
    elif char == curses.KEY_LEFT:
        left()
    elif char == curses.KEY_RIGHT:
        right()
    elif char == ord('s'):
        stop()
    elif char == ord('.'):
        reverse_left()
    elif char == ord('/'):
        reverse_right()
    
def destroy():
    GPIO.cleanup()
    
if __name__=='__main__':
    setup()
    pwm1 = GPIO.PWM(ena_l,800)
    pwm2 = GPIO.PWM(enb_l,800)
    pwm3 = GPIO.PWM(ena_r,800)
    pwm4 = GPIO.PWM(enb_r,800)
    pwm1.start(0)
    pwm2.start(0)
    pwm3.start(0)
    pwm4.start(0)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    pwm3.ChangeDutyCycle(100)
    pwm4.ChangeDutyCycle(100)
    try:
        while True:
            if GPIO.input(back_ir) == 0 or GPIO.input(front_ir) == 0:
                stop()
            else:
                control()
    except KeyboardInterrupt:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        destroy()







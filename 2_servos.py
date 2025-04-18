import RPi.GPIO as GPIO
import time

servoPINBase = 12
servoPINRot = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINBase, GPIO.OUT)
GPIO.setup(servoPINRot, GPIO.OUT)


p = GPIO.PWM(servoPINBase, 50) # GPIO 17 for PWM with 50Hz
q = GPIO.PWM(servoPINRot, 50)
p.start(5) # Initialization
q.start(5)
try:
  while True:
    
    for i in range (50, 475, 1):
      q.ChangeDutyCycle(i*0.01)
      time.sleep(0.005)
    for j in range(7, 490, 1):
      p.ChangeDutyCycle(j*0.01)
      time.sleep(0.005)
    for i in range (475, 50, -1):
      q.ChangeDutyCycle(i*0.01)
      time.sleep(0.005)
    for j in range(490, 7 , -1):
      p.ChangeDutyCycle(j*0.01)
      time.sleep(0.005)
    #q.ChangeDutyCycle(5)
    #time.sleep(0.5)
    #q.ChangeDutyCycle(7.5)
    #time.sleep(0.5)
    #q.ChangeDutyCycle(9.7)
    #time.sleep(0.5)
    
except KeyboardInterrupt:
  p.stop()
  q.stop()
  GPIO.cleanup()

import uinput
import time
import RPi.GPIO as GPIO

BTN_LEFT_CLICK=15
BTN_RIGHT_CLICK=14
BTN_UP=16
BTN_DOWN=21
BTN_LEFT=26
BTN_RIGHT=20
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_RIGHT_CLICK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_LEFT_CLICK, GPIO.IN, pull_up_down=GPIO.PUD_UP)

events = (uinput.BTN_LEFT, uinput.BTN_RIGHT, uinput.BTN_MIDDLE, uinput.REL_X, uinput.REL_Y)
deviceMouse = uinput.Device(events)

btn_left = False
btn_right = False
step = 2

while True:
  if not GPIO.input(BTN_LEFT):
    deviceMouse.emit(uinput.REL_X, -1*step)
    print("left ")    
  if not GPIO.input(BTN_RIGHT):
    deviceMouse.emit(uinput.REL_X, 1*step)
    print("right ")    
  if not GPIO.input(BTN_UP):
    deviceMouse.emit(uinput.REL_Y, -1*step)
    print("up ")    
  if not GPIO.input(BTN_DOWN):
    deviceMouse.emit(uinput.REL_Y, 1*step)
    print("down ")    
  
  if (not btn_left) and (not GPIO.input(BTN_LEFT_CLICK)):  # left button pressed
    btn_left = True
    deviceMouse.emit(uinput.BTN_LEFT, 1)
    print("left down ")
  if btn_left and GPIO.input(BTN_LEFT_CLICK):              # left button released
    btn_left = False
    deviceMouse.emit(uinput.BTN_LEFT, 0)
    print("left up ")
    
  if (not btn_right) and (not GPIO.input(BTN_RIGHT_CLICK)):  # right button pressed
    btn_right = True
    deviceMouse.emit(uinput.BTN_RIGHT, 1)
    print ("right down ")
  if btn_right and GPIO.input(BTN_RIGHT_CLICK):              # right button released
    btn_right = False
    deviceMouse.emit(uinput.BTN_RIGHT, 0)
    print ("right up ")
    
  time.sleep(.02)  # update every 20ms 

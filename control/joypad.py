
import uinput
import time
import RPi.GPIO as GPIO

BTN_FIRE1=15
BTN_FIRE2=14
BTN_UP=16
BTN_DOWN=21
BTN_LEFT=26
BTN_RIGHT=20
BTN_SELECT=3
BTN_START=19
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_FIRE1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_FIRE2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_SELECT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_START, GPIO.IN, pull_up_down=GPIO.PUD_UP)

events = (uinput.BTN_SOUTH, uinput.BTN_EAST, uinput.BTN_START, uinput.BTN_SELECT, uinput.ABS_X + (0, 100, 0, 0), uinput.ABS_Y + (0, 100, 0, 0))
device = uinput.Device(events)

fire1 = False
fire2 = False
start = False
select = False
up = False
down = False
left = False
right = False

# Center joystick
# syn=False to emit an "atomic" (50, 50) event.
device.emit(uinput.ABS_X, 50, syn=False)
device.emit(uinput.ABS_Y, 50)

while True:
  if (not start) and (not GPIO.input(BTN_START)):  # start button pressed
    start = True
    device.emit(uinput.BTN_START, 1)
  if start and GPIO.input(BTN_START):              # start button released
    start = False
    device.emit(uinput.BTN_START, 0) 
  if (not select) and (not GPIO.input(BTN_SELECT)):  # select button pressed
    select = True
    device.emit(uinput.BTN_SELECT, 1)
  if select and GPIO.input(BTN_SELECT):              # select button released
    select = False
    device.emit(uinput.BTN_SELECT, 0) 
  if (not fire1) and (not GPIO.input(BTN_FIRE1)):  # Fire1 button pressed
    fire1 = True
    device.emit(uinput.BTN_SOUTH, 1)
  if fire1 and GPIO.input(BTN_FIRE1):              # Fire1 button released
    fire1 = False
    device.emit(uinput.BTN_SOUTH, 0) 
  if (not fire2) and (not GPIO.input(BTN_FIRE2)):  # Fire2 button pressed
    fire2 = True
    device.emit(uinput.BTN_EAST, 1)
  if fire2 and GPIO.input(BTN_FIRE2):              # Fire2 button released
    fire2 = False
    device.emit(uinput.BTN_EAST, 0)
  if (not up) and (not GPIO.input(BTN_UP)):   # Up button pressed
    up = True
    device.emit(uinput.ABS_Y, 0)          # Zero Y
  if up and GPIO.input(BTN_UP):               # Up button released
    up = False
    device.emit(uinput.ABS_Y, 50)        # Center Y
  if (not down) and (not GPIO.input(BTN_DOWN)): # Down button pressed
    down = True
    device.emit(uinput.ABS_Y, 100)        # Max Y
  if down and GPIO.input(BTN_DOWN):             # Down button released
    down = False
    device.emit(uinput.ABS_Y, 50)        # Center Y
  if (not left) and (not GPIO.input(BTN_LEFT)): # Left button pressed
    left = True
    device.emit(uinput.ABS_X, 0)          # Zero X
  if left and GPIO.input(BTN_LEFT):             # Left button released
    left = False
    device.emit(uinput.ABS_X, 50)        # Center X
  if (not right) and (not GPIO.input(BTN_RIGHT)):# Right button pressed
    right = True
    device.emit(uinput.ABS_X, 100)        # Max X
  if right and GPIO.input(BTN_RIGHT):            # Right button released
    right = False
    device.emit(uinput.ABS_X, 50)        # Center X
  time.sleep(.02)  # update every 20ms

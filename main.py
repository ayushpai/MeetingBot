import time
from pynput.mouse import Button, Controller
mouse = Controller()

time.sleep(3)

def leftClick(xPos, yPos, bufferTime):
    mouse.position = (xPos, yPos)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(bufferTime)

def doubleClick(xPos, yPos, bufferTime):
    mouse.position = (xPos, yPos)
    time.sleep(1)
    mouse.click(Button.left, 2)
    time.sleep(bufferTime)

while True:
    doubleClick(1386.5546875, 311.92578125, 3) # open chrome tab3
    leftClick(1329.67578125, 114.6796875, 5) # open google cal
    leftClick(1310.46875, 392.63671875, 2) # click calendar item
    leftClick(917.6171875, 377.83203125, 4) # Join Google Meet
    leftClick(444.625, 675.79296875, 2) # Mute mic
    leftClick(517.3828125, 686.18359375, 3) # Turn off Camera
    leftClick(1034.578125, 499.55859375, 3) # Ask to join meeting

    time.sleep(10)






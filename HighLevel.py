# Import the required libraries for this script
import math, string, time, serial, win32api, win32con, re

# The port to which your Arduino board is connected
port = 'COM3'

# Invert y-axis (True/False)
invertY = False

# The cursor speed
cursorSpeed = 20

# The baudrate of the Arduino program
baudrate = 19200

# Variables indicating whether the mouse buttons are pressed or not
leftDown = False
rightDown = False

# Variables indicating the center position (no movement) of the controller
midAccelX = 530 # Accelerometer X
midAccelY = 510 # Accelerometer Y
midAnalogY = 134 # Analog Y

if port == 'arduino_port':
    print 'Please set up the Arduino port.'
    while 1:
        time.sleep(1)

# Connect to the serial port
ser = serial.Serial(port, baudrate, timeout = 1)

# Wait 1s for things to stabilize
time.sleep(1)

# While the serial port is open
while ser.isOpen():

    # Read one line
    line = ser.readline()

    # Strip the ending (\r\n)
    line = string.strip(line, '\r\n')

    # Split the string into an array containing the data from the Wii Nunchuk
    line = string.split(line, ' ')

    # Set variables for each of the values
    analogX = int(re.sub("\D", "", line[0]))
    analogY = int(re.sub("\D", "", line[1]))
    accelX = int(re.sub("\D", "", line[2]))
    accelY = int(re.sub("\D", "", line[3]))
    accelZ = int(re.sub("\D", "", line[4]))
    zButton = int(re.sub("\D", "", line[5]))
    cButton = int(re.sub("\D", "", line[6]))


    # Left Mouse Button
    # If the Wii Nunchuk Z Button is pressed, but wasn't previously
    if(zButton and not leftDown):
        # Simulate a mouse pressing the left mouse button
        leftDown = True
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    # Else if it was pressed, but isn't anymore
    elif(leftDown and not zButton):
        # Simulate a mouse releasing the left mouse button
        leftDown = False
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)


    # Right Mouse Button
    # Do the same with the C Button, simulating the right mouse button
    if(cButton and not rightDown):
        rightDown = True
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    elif(rightDown and not cButton):
        rightDown = False
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
        

    # Mouse Wheel
    # If the analog stick is not centered
    if(abs(analogY - midAnalogY) > 5):
        # Simulate a mouse wheel movement
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,int(math.floor((analogY - midAnalogY)/2)),0)
    else:
        # Simulate a mouse wheel stopped
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,0,0)


    # Mouse Movement
    # Create variables indicating how much the mouse cursor should move in each direction
    dx = 0
    dy = 0

    # If the Wii Nunchuk is rotated around the x-axis
    if(abs(accelX - midAccelX) > 20):
        # Calculate how much the cursor should move horizontally
        dx = int(math.floor((accelX - midAccelX)*cursorSpeed/400))

    # If the Wii Nunchuk is rotated around the y-axis
    if(abs(accelY - midAccelY) > 20):
        # Calculate how much the cursor should move vertically
        dy = int(math.floor((accelY - midAccelY)*cursorSpeed/400))
        # Invert the y-axis
        if invertY:
            dy = dy*-1

    # Simulate mouse movement with the values calculated above
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,dx,dy,0,0)
    

# After the program is over, close the serial port connection
ser.close()
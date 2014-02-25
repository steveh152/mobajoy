# Import the required libraries for this script
import math, string, time, serial, win32api, win32con, re
from threading import Timer

def mover(angle):
    '''
    Maps the angle of the analog stick to a location in a ring around the player
                          _  _  _

                          |  p  |
                          _  _  _
    The location in the ring is clicked and the cursor is moved back to its original position
    '''
    radius=60
    centerX= 1600/2
    centerY= 900/2

    last= win32api.GetCursorPos()
    if (angle!= None):
        x= centerX+int(math.sin(angle)*radius)
        y= centerY+int(math.cos(angle)*radius)
        print x, y, last
        win32api.SetCursorPos((x,y))
        #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        print "click"
        # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
        print "unclick"
        win32api.SetCursorPos(last)





# The port to which your Arduino board is connected
port = 'COM3'

# The baudrate of the Arduino program
baudrate = 19200

# Variables indicating whether the mouse buttons are pressed or not
leftDown = False
rightDown = False

# Variables indicating the center position (no movement) of the controller
midAnalogY = 130 # Analog Y
midAnalogX = 129 # Analog X

# Variables indicating tolerance to begin to detect movement
tolAnalog = 15


# Connect to the serial port
ser = serial.Serial(port, baudrate, timeout = 1)

# Wait 1s for things to stabilize
time.sleep(1)

# While the serial port is open
while ser.isOpen():

    # Runs function every so often
    time.sleep(0.1)


    # Read one line
    line = ser.readline()

    # Strip the ending (\r\n)
    line = string.strip(line, '\r\n')

    # Split the string into an array containing the data from the Wii Nunchuk
    line = string.split(line, ' ')

    # Set variables for each of the values and remove extra artifacts from the stream
    try:
        analogX = int(re.sub("\D", "", line[0]))
        analogY = int(re.sub("\D", "", line[1]))
        accelX = int(re.sub("\D", "", line[2]))
        accelY = int(re.sub("\D", "", line[3]))
        accelZ = int(re.sub("\D", "", line[4]))
        zButton = int(re.sub("\D", "", line[5]))
        cButton = int(re.sub("\D", "", line[6]))
    # If values from current serial line cannot be read, program skips to next serial line
    except ValueError:
        continue
    except IndexError:
        continue

    # Adjusts coordinates so the origin is 0
    xCoo= analogX-midAnalogX
    yCoo= analogY-midAnalogY

    #converts the cartesian coordinate to an angular coordinate
    angle= None
    if ((abs(xCoo) > tolAnalog) or (abs(yCoo) > tolAnalog)):
        angle= math.atan2(yCoo, xCoo)

    
    #Passes an angle value off to the next function 
    mover(angle)

# After the program is over, close the serial port connection
ser.close()
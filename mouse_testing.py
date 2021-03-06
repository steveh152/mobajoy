import win32api, win32con, time

# ***look into win32api.LoadCursor***

def get_screen_size():
	width = win32api.GetSystemMetrics(0)
	height = win32api.GetSystemMetrics(1)
	return (width, height)

def print_mouse_pos():
	(x,y) = win32api.GetCursorPos()
	print "x:", str(x)," |  y:", str(y)

def print_key():
	for num in range(0,127):
		press = win32api.GetAsyncKeyState(num)
		if press != 0:
			print num

# function to click a side of the screen and then return the cursor
def click_and_return(direction, width, height):
	(_x,_y) = win32api.GetCursorPos()
	if (direction == "right"):
		print "right"
		x = width - 20
		y = height/2
	elif (direction == "left"):
		print "left"
		x = 20
		y = height/2
	elif (direction == "up"):
		print "up"
		x = width/2
		y = 20
	elif (direction == "down"):
		print "down"
		x = width/2
		y = height - 20
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
	time.sleep(0.1)
	win32api.SetCursorPos((_x,_y))

# function to detect what key user has pressed
def detect_keypress(direction_old):
	direction = direction_old
	while direction == direction_old:
		if win32api.GetAsyncKeyState(38) != 0:
			print "trying up"
			direction = "up"
		elif win32api.GetAsyncKeyState(37) != 0:
			print "trying left"
			direction = "left"
		elif win32api.GetAsyncKeyState(40) != 0:
			print "trying down"
			direction = "down"
		elif win32api.GetAsyncKeyState(39) != 0:
			print "trying right"
			direction = "right"
		elif win32api.GetAsyncKeyState(27) != 0:
			return "stop"
		time.sleep(0.05)
	return direction


# ===========================================
# Main Code
# ===========================================
(width, height) = get_screen_size()
direction = "null"
direction_old = "null"
while True:
	print "start"
	direction = detect_keypress(direction_old)
	print "stop"
	if direction == "stop":
		break
	click_and_return(direction, width, height)
	direction_old = direction

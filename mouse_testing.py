import win32api, win32con

# look into win32api.LoadCursor

def click_and_return(x,y):
	(_x,_y) = win32api.GetCursorPos()
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
	win32api.SetCursorPos((_x,_y))

click_and_return(10,10)


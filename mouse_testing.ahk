;==================================================================
; FUNCTIONS 
;==================================================================

window_click()
{
	MsgBox, OK, "about to click", %dir_str%
	ControlClick, x55 y77, right, A
	MsgBox, OK, "just clicked", %dir_str%
}

click_and_return(dir)
{
	; define limits of screen resolution
	;x_mid = %A_ScreenWidth%/2
	x_mid = 640
	;y_mid = %A_ScreenHeight%/2
	y_mid = 400
	;x_max = %A_ScreenWidth% - 20
	x_max = 1260
	;y_max = %A_ScreenHeight% - 20
	y_max = 780

	x_res = %A_ScreenWidth%
	y_res = %A_ScreenHeight%
	resolutions = x: %x_res%   y: %y_res%
	;MsgBox, OK, "Screen Res", %resolutions%

	; find location of mouse
	MouseGetPos, x_loc, y_loc
	; right-click mouse in correct position depending on direction
	; FOR CONTROLCLICK: use winspector to find window name, controls, etc.
	if (dir == "up") {
		dir_str = UP:  x = %x_mid%   y = %20%
		;MsgBox, OK, "direction/location", %dir_str%
		MouseMove, x_mid, 20, 0
		Click right
	}
	else if (dir == "down") {
		dir_str = DOWN:  x = %x_mid%   y = %y_max%
		MouseMove, x_mid, y_max, 0
		Click right
	}
	else if (dir == "left") {
		dir_str = LEFT:  x = 20   y = %y_mid%
		MouseMove, 20, y_mid, 0
		Click right
	}
	else if (dir == "right") {
		dir_str = RIGHT:  x = %x_max%   y = %y_mid%
		MouseMove, x_max, y_mid, 0
		Click right
	}
	; return mouse to previous location
	MouseMove, x_loc, y_loc, 0
}

move_while_pressed(btn, dir)
{
	; define center of screen
	;x_mid = %A_ScreenWidth%/2
	x_mid = 640
	;y_mid = %A_ScreenHeight%/2
	y_mid = 400

	while (GetKeyState(btn, "P"))
	{
		;right-click in direction given
		click_and_return(dir)

		;Wait for x seconds, x being about the amount of time it takes
		;for the character to get to the waypoint. Wait this time in 
		;increments, so that if the button is released at any time the
		;wait will terminate.
		time = 0
		while (time < 2500 && GetKeyState(btn, "P"))
		{
			;sleep for 0.1 seconds
			Sleep, 100
			time += 100
		}
	}

	;Msgbox, OK, "here"
	;find current location of mouse
	MouseGetPos, x_loc, y_loc

	;Right-click on character, this should stop movement. Character
	;should be in center of screen, this script assumes camera lock
	;on character.
	MouseMove, x_mid, y_mid, 0
	Click right

	;move mouse back to previous position
	MouseMove, x_loc, y_loc, 0
}


;==================================================================
; MAIN CODE
;==================================================================

; sets mouse to use entire screen for coordinates
CoordMode, Mouse, Screen

; detect button press and move accordingly
$Up::move_while_pressed("Up", "up")
$Down::move_while_pressed("Down", "down")
$Left::move_while_pressed("Left", "left")
$Right::move_while_pressed("Right", "right")
; try out controlclick
Home::window_click()

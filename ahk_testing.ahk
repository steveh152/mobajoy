/* Test functionality of ControlClick
#NoEnv
SetTitleMatchMode, 2
SendMode Input
SetWorkingDir %A_ScriptDir%

postplease()
{
	Msgbox, OK, "about to click", "clickey-clack"
	PostMessage, 0x21, ahk_class WMPlayerApp
	return

}
*/

test_keypress()
{
	Loop {
		if not GetKeyState("End", "P")
			break
		Click
	}
	return	
}

;#IfWinActive ahk_class MozillaUIWindowClass
$End::test_keypress()

from pyunicon.util.UCKeyCode import UCKeyCode

# unix codes:
# http://unix.stackexchange.com/questions/130656/how-to-get-all-my-keys-to-send-keycodes

# names: https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py

# cocoa codes:
# http://boredzo.org/blog/archives/2007-05-22/virtual-key-codes

# --- Flag Keys ---
UC_LEFT_SHIFT = UCKeyCode('Shift_L', cocoa=56, x11=None, win32=None)
UC_RIGHT_SHIFT = UCKeyCode('Shift_R', cocoa=56, x11=None, win32=None)

UC_LEFT_CONTROL = UCKeyCode('Control_L', cocoa=59, x11=None, win32=None)
UC__RIGHT_CONTROL = UCKeyCode('Control_R', cocoa=59, x11=None, win32=None)

UC_LEFT_ALT = UCKeyCode('ALT_L', cocoa=58, x11=None, win32=None)
UC_RIGHT_ALT = UCKeyCode('ALT_R', cocoa=58, x11=None, win32=None)

UC_LEFT_COMMAND = UCKeyCode('Super_L', cocoa=55, x11=None, win32=None)
UC_RIGHT_COMMAND = UCKeyCode('Super_R', cocoa=55, x11=None, win32=None)

UC_CAPSLOCK = UCKeyCode('Caps_Lock', cocoa=57, x11=None, win32=None)

# --- Command Keys ---
UC_TAB = UCKeyCode('Tab', cocoa=48, x11=None, win32=None)
UC_RETURN = UCKeyCode('Return', cocoa=36, x11=None, win32=None)
UC_ESCAPE = UCKeyCode('Escape', cocoa=53, x11=None, win32=None)
UC_DELETE = UCKeyCode('Delete', cocoa=51, x11=None, win32=None)
UC_SPACE = UCKeyCode('space', cocoa=49, x11=None, win32=None)

# --- Arrow Keys ---
UC_UP = UCKeyCode('Up', cocoa=126, x11=None, win32=None)
UC_DOWN = UCKeyCode('Down', cocoa=125, x11=None, win32=None)
UC_LEFT = UCKeyCode('Left', cocoa=123, x11=None, win32=None)
UC_RIGHT = UCKeyCode('Right', cocoa=124, x11=None, win32=None)

# --- Special Signs ---
UC_EQUALS = UCKeyCode('equal', cocoa=24, x11=None, win32=None)
UC_MINUS = UCKeyCode('minus', cocoa=27, x11=None, win32=None)
UC_LEFTBRACKET = UCKeyCode('bracketleft', cocoa=33, x11=None, win32=None)
UC_RIGHTBRACKET = UCKeyCode('bracketright', cocoa=30, x11=None, win32=None)
UC_APOSTROPHE = UCKeyCode('apostrophe', cocoa=39, x11=None, win32=None)
UC_SEMICOLON = UCKeyCode('semicolon', cocoa=41, x11=None, win32=None)
UC_FRONTSLASH = UCKeyCode('slash', cocoa=42, x11=None, win32=None)
UC_COMMA = UCKeyCode('comma', cocoa=43, x11=None, win32=None)
UC_BACKSLASH = UCKeyCode('backslash', cocoa=44, x11=None, win32=None)
UC_PERIOD = UCKeyCode('period', cocoa=47, x11=None, win32=None)
UC_BACKAPOSTROPHE = UCKeyCode('grave', cocoa=50, x11=None, win32=None)

# --- Numbers ---
UC_0 = UCKeyCode('0', cocoa=29, x11=None, win32=None)
UC_1 = UCKeyCode('1', cocoa=18, x11=None, win32=None)
UC_2 = UCKeyCode('2', cocoa=19, x11=None, win32=None)
UC_3 = UCKeyCode('3', cocoa=20, x11=None, win32=None)
UC_4 = UCKeyCode('4', cocoa=21, x11=None, win32=None)
UC_5 = UCKeyCode('5', cocoa=23, x11=None, win32=None)
UC_6 = UCKeyCode('6', cocoa=22, x11=None, win32=None)
UC_7 = UCKeyCode('7', cocoa=26, x11=None, win32=None)
UC_8 = UCKeyCode('8', cocoa=28, x11=None, win32=None)
UC_9 = UCKeyCode('9', cocoa=25, x11=None, win32=None)

# --- ABC ---
UC_A = UCKeyCode('a', cocoa=0, x11=None, win32=None)
UC_B = UCKeyCode('b', cocoa=11, x11=None, win32=None)
UC_C = UCKeyCode('c', cocoa=8, x11=None, win32=None)
UC_D = UCKeyCode('d', cocoa=2, x11=None, win32=None)
UC_E = UCKeyCode('e', cocoa=14, x11=None, win32=None)
UC_F = UCKeyCode('f', cocoa=3, x11=None, win32=None)
UC_G = UCKeyCode('g', cocoa=5, x11=None, win32=None)
UC_H = UCKeyCode('h', cocoa=4, x11=None, win32=None)
UC_I = UCKeyCode('i', cocoa=34, x11=None, win32=None)
UC_J = UCKeyCode('j', cocoa=38, x11=None, win32=None)
UC_K = UCKeyCode('k', cocoa=40, x11=None, win32=None)
UC_L = UCKeyCode('l', cocoa=37, x11=None, win32=None)
UC_M = UCKeyCode('m', cocoa=46, x11=None, win32=None)
UC_N = UCKeyCode('n', cocoa=45, x11=None, win32=None)
UC_O = UCKeyCode('o', cocoa=31, x11=None, win32=None)
UC_P = UCKeyCode('p', cocoa=35, x11=None, win32=None)
UC_Q = UCKeyCode('q', cocoa=12, x11=None, win32=None)
UC_R = UCKeyCode('r', cocoa=15, x11=None, win32=None)
UC_S = UCKeyCode('s', cocoa=1, x11=None, win32=None)
UC_T = UCKeyCode('t', cocoa=17, x11=None, win32=None)
UC_U = UCKeyCode('u', cocoa=32, x11=None, win32=None)
UC_V = UCKeyCode('v', cocoa=9, x11=None, win32=None)
UC_W = UCKeyCode('w', cocoa=13, x11=None, win32=None)
UC_X = UCKeyCode('x', cocoa=7, x11=None, win32=None)
UC_Y = UCKeyCode('y', cocoa=16, x11=None, win32=None)
UC_Z = UCKeyCode('z', cocoa=6, x11=None, win32=None)
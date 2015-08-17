from pyunicon.util.UCKeyCode import UCKeyCode

# unix codes:
# http://unix.stackexchange.com/questions/130656/how-to-get-all-my-keys-to-send-keycodes

# cocoa codes:
# http://boredzo.org/blog/archives/2007-05-22/virtual-key-codes

# --- Flag Keys ---
UC_LEFT_SHIFT = UCKeyCode(56, 42, None)
UC_RIGHT_SHIFT = UCKeyCode(56, 54, None)

UC_LEFT_CONTROL = UCKeyCode(59, 29, None)
UC__RIGHT_CONTROL = UCKeyCode(59, 97, None)

UC_LEFT_OPTION = UCKeyCode(58, 56, None)
UC_RIGHT_OPTION = UCKeyCode(58, 100, None)

# todo: find uckeycode command for unix
UC_LEFT_COMMAND = UCKeyCode(55, None, None)
UC_RIGHT_COMMAND = UCKeyCode(55, None, None)

UC_CAPSLOCK = UCKeyCode(57, 58, None)

# --- Command Keys ---
UC_TAB = UCKeyCode(48, 15, None)
UC_RETURN = UCKeyCode(36, 28, None)
UC_ESCAPE = UCKeyCode(53, 1, None)
UC_DELETE = UCKeyCode(51, 111, None)
UC_SPACE = UCKeyCode(49, 57, None)

# --- Arrow Keys ---
UC_UP = UCKeyCode(126, 103, None)
UC_DOWN = UCKeyCode(125, 108, None)
UC_LEFT = UCKeyCode(123, 105, None)
UC_RIGHT = UCKeyCode(124, 106, None)

# --- Special Signs ---
UC_EQUALS = UCKeyCode(24, 13, None)
UC_MINUS = UCKeyCode(27, 12, None)
UC_LEFTBRACKET = UCKeyCode(33, 26, None)
UC_RIGHTBRACKET = UCKeyCode(30, 27, None)
UC_APOSTROPHE = UCKeyCode(39, 40, None)
UC_SEMICOLON = UCKeyCode(41, 39, None)
UC_FRONTSLASH = UCKeyCode(42, 53, None)
UC_COMMA = UCKeyCode(43, 51, None)
UC_BACKSLASH = UCKeyCode(44, 43, None)
UC_PERIOD = UCKeyCode(47, 52, None)
UC_BACKAPOSTROPHE = UCKeyCode(50, None, None)

# --- Numbers ---
UC_0 = UCKeyCode(29, 11, None)
UC_1 = UCKeyCode(18, 2, None)
UC_2 = UCKeyCode(19, 3, None)
UC_3 = UCKeyCode(20, 4, None)
UC_4 = UCKeyCode(21, 5, None)
UC_5 = UCKeyCode(23, 6, None)
UC_6 = UCKeyCode(22, 7, None)
UC_7 = UCKeyCode(26, 8, None)
UC_8 = UCKeyCode(28, 9, None)
UC_9 = UCKeyCode(25, 10, None)

# --- ABC ---
UC_A = UCKeyCode(0, 30, None)
UC_B = UCKeyCode(11, 48, None)
UC_C = UCKeyCode(8, 46, None)
UC_D = UCKeyCode(2, 32, None)
UC_E = UCKeyCode(14, 18, None)
UC_F = UCKeyCode(3, 33, None)
UC_G = UCKeyCode(5, 34, None)
UC_H = UCKeyCode(4, 35, None)
UC_I = UCKeyCode(34, 23, None)
UC_J = UCKeyCode(38, 36, None)
UC_K = UCKeyCode(40, 37, None)
UC_L = UCKeyCode(37, 38, None)
UC_M = UCKeyCode(46, 50, None)
UC_N = UCKeyCode(45, 49, None)
UC_O = UCKeyCode(31, 24, None)
UC_P = UCKeyCode(35, 25, None)
UC_Q = UCKeyCode(12, 16, None)
UC_R = UCKeyCode(15, 19, None)
UC_S = UCKeyCode(1, 31, None)
UC_T = UCKeyCode(17, 20, None)
UC_U = UCKeyCode(32, 22, None)
UC_V = UCKeyCode(9, 47, None)
UC_W = UCKeyCode(13, 17, None)
UC_X = UCKeyCode(7, 45, None)
UC_Y = UCKeyCode(16, 21, None)
UC_Z = UCKeyCode(6, 44, None)

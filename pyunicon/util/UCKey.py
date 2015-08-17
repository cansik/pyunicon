__enum_index = 0


def next_index():
    global __enum_index
    __enum_index += 1
    return __enum_index


# --- Flag Keys ---
UC_SHIFT = next_index()
UC_CONTROL = next_index()
UC_OPTION = next_index()
UC_COMMAND = next_index()
UC_CAPSLOCK = next_index()

# --- Command Keys ---
UC_TAB = next_index()
UC_RETURN = next_index()
UC_ESCAPE = next_index()
UC_DELETE = next_index()

# --- Arrow Keys ---
UC_UP = next_index()
UC_DOWN = next_index()
UC_LEFT = next_index()
UC_RIGHT = next_index()

# --- Special Signs ---
UC_EQUALS = next_index()
UC_MINUS = next_index()
UC_RIGHTBRACKET = next_index()
UC_LEFTBRACKET = next_index()
UC_APOSTROPHE = next_index()
UC_SEMICOLON = next_index()
UC_FRONTSLASH = next_index()
UC_COMMA = next_index()
UC_BACKSLASH = next_index()
UC_PERIOD = next_index()
UC_BACKAPOSTROPHE = next_index()

# --- Numbers ---
UC_0 = next_index()
UC_1 = next_index()
UC_2 = next_index()
UC_3 = next_index()
UC_4 = next_index()
UC_5 = next_index()
UC_6 = next_index()
UC_7 = next_index()
UC_8 = next_index()
UC_9 = next_index()

# --- ABC ---
UC_A = next_index()
UC_B = next_index()
UC_C = next_index()
UC_D = next_index()
UC_E = next_index()
UC_F = next_index()
UC_G = next_index()
UC_H = next_index()
UC_I = next_index()
UC_J = next_index()
UC_K = next_index()
UC_L = next_index()
UC_M = next_index()
UC_N = next_index()
UC_O = next_index()
UC_P = next_index()
UC_Q = next_index()
UC_R = next_index()
UC_S = next_index()
UC_T = next_index()
UC_U = next_index()
UC_V = next_index()
UC_W = next_index()
UC_X = next_index()
UC_Y = next_index()
UC_Z = next_index()

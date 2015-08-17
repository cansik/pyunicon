from pyunicon.util import UCKey
import pyunicon.util.UCKey


class CocoaKeyCodeConverter(object):
    @staticmethod
    def convert(key_code):
        # key are defined here:
        # http://boredzo.org/blog/archives/2007-05-22/virtual-key-codes

        # --- Flag Keys ---
        if key_code is UCKey.UC_COMMAND: return 55
        if key_code is UCKey.UC_SHIFT: return 56
        if key_code is UCKey.UC_CAPSLOCK: return 57
        if key_code is UCKey.UC_OPTION: return 58
        if key_code is UCKey.UC_CONTROL: return 59

        # --- Command Keys ---
        if key_code is UCKey.UC_TAB: return 48
        if key_code is UCKey.UC_DELETE: return 51
        if key_code is UCKey.UC_ESCAPE: return 53
        if key_code is UCKey.UC_RETURN: return 36

        # --- Arrow Keys ---
        if key_code is UCKey.UC_UP: return 126
        if key_code is UCKey.UC_DOWN: return 125
        if key_code is UCKey.UC_LEFT: return 123
        if key_code is UCKey.UC_RIGHT: return 12

        # --- Special Signs ---
        if key_code is UCKey.UC_EQUALS: return 24
        if key_code is UCKey.UC_MINUS: return 27
        if key_code is UCKey.UC_RIGHTBRACKET: return 30
        if key_code is UCKey.UC_LEFTBRACKET: return 33
        if key_code is UCKey.UC_APOSTROPHE: return 39
        if key_code is UCKey.UC_SEMICOLON: return 41
        if key_code is UCKey.UC_FRONTSLASH: return 42
        if key_code is UCKey.UC_COMMA: return 43
        if key_code is UCKey.UC_BACKSLASH: return 44
        if key_code is UCKey.UC_PERIOD: return 47
        if key_code is UCKey.UC_BACKAPOSTROPHE: return 50

        # --- Numbers ---
        if key_code is UCKey.UC_1: return 18
        if key_code is UCKey.UC_2: return 19
        if key_code is UCKey.UC_3: return 20
        if key_code is UCKey.UC_4: return 21
        if key_code is UCKey.UC_6: return 22
        if key_code is UCKey.UC_5: return 23
        if key_code is UCKey.UC_9: return 25
        if key_code is UCKey.UC_7: return 26
        if key_code is UCKey.UC_8: return 28
        if key_code is UCKey.UC_0: return 29

        # --- ABC ---
        if key_code is UCKey.UC_A: return 0
        if key_code is UCKey.UC_S: return 1
        if key_code is UCKey.UC_D: return 2
        if key_code is UCKey.UC_F: return 3
        if key_code is UCKey.UC_H: return 4
        if key_code is UCKey.UC_G: return 5
        if key_code is UCKey.UC_Z: return 6
        if key_code is UCKey.UC_X: return 7
        if key_code is UCKey.UC_C: return 8
        if key_code is UCKey.UC_V: return 9
        if key_code is UCKey.UC_B: return 11
        if key_code is UCKey.UC_Q: return 12
        if key_code is UCKey.UC_W: return 13
        if key_code is UCKey.UC_E: return 14
        if key_code is UCKey.UC_R: return 15
        if key_code is UCKey.UC_Y: return 16
        if key_code is UCKey.UC_T: return 17
        if key_code is UCKey.UC_O: return 31
        if key_code is UCKey.UC_U: return 32
        if key_code is UCKey.UC_I: return 34
        if key_code is UCKey.UC_P: return 35
        if key_code is UCKey.UC_L: return 37
        if key_code is UCKey.UC_J: return 38
        if key_code is UCKey.UC_K: return 40
        if key_code is UCKey.UC_N: return 45
        if key_code is UCKey.UC_M: return 46

        return None

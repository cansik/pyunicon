from ctypes import *
import time

from Xlib.display import Display
import Xlib
from Xlib import X
import Xlib.XK

# custom types
t_Atom = c_ulong
t_Bool = c_int
t_Display = c_void_p
t_Window = c_ulong
t_Colormap = c_ulong


class X11Util(object):
    def __init__(self):
        self.__xlib = cdll.LoadLibrary('libX11.so.6')
        self.__display = self.open_display()
        self.__window = self.__xlib.XDefaultRootWindow(self.__display)

    def xsend_event(self, key_code, is_down):
        # based on the idea of http://stackoverflow.com/a/30281261/1138326
        key = XEvent(type=2).xkey
        key.keycode = self.__xlib.XKeysymToKeycode(self.__display, key_code)
        key.window = key.root = self.__xlib.XDefaultRootWindow(self.__display)
        self.__xlib.XSendEvent(self.__display, key.window, True, 1, byref(key))

    def send_key(self, emulated_key):
        display = Display()
        root = display.screen().root

        shift_mask = 0  # or Xlib.X.ShiftMask
        window = display.get_input_focus()._data["focus"]
        keysym = Xlib.XK.string_to_keysym(emulated_key)
        keycode = display.keysym_to_keycode(keysym)

        Xlib.ext.xtest.fake_input(window, Xlib.X.KeyPress, keycode)

        event = Xlib.protocol.event.KeyPress(
            time=int(time.time()),
            root=root,
            window=window,
            same_screen=0, child=Xlib.X.NONE,
            root_x=0, root_y=0, event_x=0, event_y=0,
            state=shift_mask,
            detail=keycode
        )
        window.send_event(event, propagate=True)
        event = Xlib.protocol.event.KeyRelease(
            time=int(time.time()),
            root=display.screen().root,
            window=window,
            same_screen=0, child=Xlib.X.NONE,
            root_x=0, root_y=0, event_x=0, event_y=0,
            state=shift_mask,
            detail=keycode
        )
        window.send_event(event, propagate=True)
        display.sync()

    def get_xwindow_attributes(self):
        xwa = XWindowAttributes()
        self.__xlib.XGetWindowAttributes(self.__display, self.__window, byref(xwa))
        return xwa

    def xwarp_pointer(self, x, y):
        self.__xlib.XWarpPointer(self.__display, None, self.__window, 0, 0, 0, 0, int(x), int(y))

    def xquery_pointer(self):
        (root_id, child_id) = (c_uint32(), c_uint32())
        (root_x, root_y, win_x, win_y) = (c_int(), c_int(), c_int(), c_int())
        mask = c_uint()
        self.__xlib.XQueryPointer(self.__display, c_uint32(self.__window), byref(root_id), byref(child_id),
                                  byref(root_x), byref(root_y),
                                  byref(win_x), byref(win_y), byref(mask))
        return root_x, root_y, win_x, win_y

    def open_display(self):
        return self.__xlib.XOpenDisplay(None)

    def close_display(self):
        self.__xlib.XCloseDisplay(self.__display)


class XWindowAttributes(Structure):
    _fields_ = [
        ('x', c_int),
        ('y', c_int),
        ('width', c_int),
        ('height', c_int),
        ('border_width', c_int),
        ('depth', c_int),
        ('visual', c_void_p),
        ('root', t_Window),
        ('class', c_int),
        ('bit_gravity', c_int),
        ('win_gravity', c_int),
        ('backing_store', c_int),
        ('backing_planes', c_ulong),
        ('backing_pixel', c_ulong),
        ('save_under', t_Bool),
        ('colormap', t_Colormap),
        ('map_installed', t_Bool),
        ('map_state', c_int),
        ('all_event_masks', c_long),
        ('your_event_masks', c_long),
        ('do_not_propagate_mask', c_long),
        ('override_redirect', t_Bool),
        ('screen', c_void_p),
    ]


class XKeyEvent(Structure):
    _fields_ = [
        ('type', c_int),
        ('serial', c_ulong),
        ('send_event', c_int),
        ('display', c_void_p),
        ('window', c_ulong),
        ('root', c_ulong),
        ('subwindow', c_ulong),
        ('time', c_ulong),
        ('x', c_int),
        ('y', c_int),
        ('x_root', c_int),
        ('y_root', c_int),
        ('state', c_uint),
        ('keycode', c_uint),
        ('same_screen', c_int),
    ]


class XEvent(Union):
    _fields_ = [
        ('type', c_int),
        ('xkey', XKeyEvent),
        ('pad', c_long * 24),
    ]

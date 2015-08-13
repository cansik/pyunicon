from ctypes import *

# custom types
t_Atom = c_ulong
t_Bool = c_int
t_Display = c_void_p
t_Window = c_ulong
t_Colormap = c_ulong


class X11Util(object):
    def __init__(self):
        self.__xlib = cdll.LoadLibrary('libX11.so')
        self.__display = self.open_display()
        self.__window = self.__xlib.XDefaultRootWindow(self.__display)

    def get_xwindow_attributes(self):
        xwa = self.XWindowAttributes()
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
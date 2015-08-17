from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGEventRightMouseDown
from Quartz.CoreGraphics import kCGEventRightMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import CGEventCreate
from Quartz.CoreGraphics import CGEventGetLocation
from Quartz.CoreGraphics import CGWarpMouseCursorPosition
from pyunicon.util import UCMouseKey

__author__ = 'cansik'


class CocoaMouse(object):
    def __init__(self):
        pass

    def __mouse_event(self, type, x, y):
        mouse_event = CGEventCreateMouseEvent(None, type, (x, y), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, mouse_event)

    def move(self, x, y):
        self.__mouse_event(kCGEventMouseMoved, x, y)
        CGWarpMouseCursorPosition((x, y))
        # todo: fix race condition (get position is not accurate)

    def get_position(self):
        mouse_event = CGEventCreate(None)
        pos = CGEventGetLocation(mouse_event)
        return pos.x, pos.y

    def press(self, mouse_key):
        x, y = self.get_position()

        if mouse_key is UCMouseKey.UC_MOUSE_LEFT:
            self.__mouse_event(kCGEventLeftMouseDown, x, y)
        elif mouse_key is UCMouseKey.UC_MOUSE_MIDDLE:
            print("mouse middle not supported on OSX!")
        elif mouse_key is UCMouseKey.UC_MOUSE_RIGHT:
            self.__mouse_event(kCGEventRightMouseDown, x, y)

    def release(self, mouse_key):
        x, y = self.get_position()

        if mouse_key is UCMouseKey.UC_MOUSE_LEFT:
            self.__mouse_event(kCGEventLeftMouseUp, x, y)
        elif mouse_key is UCMouseKey.UC_MOUSE_MIDDLE:
            print("mouse middle not supported on OSX!")
        elif mouse_key is UCMouseKey.UC_MOUSE_RIGHT:
            self.__mouse_event(kCGEventRightMouseUp, x, y)

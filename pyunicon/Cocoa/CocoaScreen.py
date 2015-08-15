from Quartz import CGDisplayBounds
from Quartz import CGMainDisplayID

__author__ = 'cansik'


class CocoaScreen(object):
    def __init__(self):
        pass

    def get_size(self):
        main_monitor = CGDisplayBounds(CGMainDisplayID())
        return main_monitor.size.width, main_monitor.size.height

from time import sleep
from pyunicon.UCMouse import UCMouse

__author__ = 'cansik'

mouse = UCMouse()
mouse.move(200, 200)
print('X, Y: %s, %s' % mouse.get_position())
print('sleeping...')
print('moving...')
mouse.move(1000, 300)
print('X, Y: %s, %s' % mouse.get_position())
mouse.move(5, 200)
print('X, Y: %s, %s' % mouse.get_position())
print('clicking...')
mouse.click_left()


from time import sleep
from pyunicon.UCMouse import UCMouse

__author__ = 'cansik'

mouse = UCMouse()
x, y = mouse.get_position()
mouse.move(200, 200)
sleep(1)
mouse.move(300, 300)
mouse.click_left()

print('X, Y: %s, %s' % (x, y))

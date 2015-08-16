from time import sleep
from pyunicon.UCKeyboard import UCKeyboard
from pyunicon.UCMouse import UCMouse
from pyunicon.UCScreen import UCScreen

__author__ = 'cansik'

screen = UCScreen()
print(screen.get_size())

sleep(1)

mouse = UCMouse()
print('X, Y: %s, %s' % mouse.get_position())
mouse.move(200, 200)
print('X, Y: %s, %s' % mouse.get_position())
print('sleeping...')
print('moving...')
mouse.move(1000, 300)
print('X, Y: %s, %s' % mouse.get_position())
mouse.move(29, 594)
print('X, Y: %s, %s' % mouse.get_position())
print('clicking...')

mouse.click_left()

sleep(1)

keyboard = UCKeyboard()
print("send key")

keyboard.send_key(36)
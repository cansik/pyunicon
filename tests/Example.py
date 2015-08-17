from time import sleep
from pyunicon.UCKeyboard import UCKeyboard
from pyunicon.UCMouse import UCMouse
from pyunicon.UCScreen import UCScreen
from pyunicon.util import UCKey

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

keyboard.key_down(UCKey.UC_LEFT_SHIFT)
keyboard.send_key(UCKey.UC_H)
keyboard.key_up(UCKey.UC_LEFT_SHIFT)
keyboard.send_key(UCKey.UC_A)
keyboard.send_key(UCKey.UC_L)
keyboard.send_key(UCKey.UC_L)
keyboard.send_key(UCKey.UC_O)
keyboard.send_key(UCKey.UC_SPACE)
keyboard.send_key(UCKey.UC_W)
keyboard.send_key(UCKey.UC_O)
keyboard.send_key(UCKey.UC_R)
keyboard.send_key(UCKey.UC_L)
keyboard.send_key(UCKey.UC_D)
keyboard.send_key(UCKey.UC_RETURN)
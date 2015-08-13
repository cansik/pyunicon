from pyunicon.UCMouse import UCMouse

__author__ = 'cansik'

mouse = UCMouse()
print(mouse.get_mouse_position())
mouse.move_mouse(200, 200)

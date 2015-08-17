# PyUnicon
PyUnicon is a cross platform library to control keyboard and mouse. Works on MacOSX (Cocoa), Linux (X11) and Windows (Win32)

#### Install

The easiest way is to install by [PIP](https://pypi.python.org/pypi/pyunicon/0.1.0):

```
pip install pyunicon
```

#### Example

```
mouse = UCMouse()
x, y = mouse.get_position()
mouse.move(200, 200)
sleep(1)
mouse.move(300, 300)
mouse.click_left()

print('X, Y: %s, %s' % (x, y))
```

#### What can you do?

* Mouse
 * move
 * click left
 * click right
 * get position
* Keyboard
 * key down
 * key up
 * send key 
* Screen
 * get size
* App
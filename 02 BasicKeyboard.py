import pyautogui as pg

print(pg.position())
# pg.click(1397,79,duration=3)
# pg.typewrite('Hello World')
# pg.write('hi world', interval=1)
# pg.hotkey('ctrlleft','a')
# pg.hotkey('altleft','up')
# pg.press('hhh')

pg.click(41,122,duration=5)
pg.write(f'''PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. The API is designed to be simple. PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
To install with pip, run pip install pyautogui. See the Installation page for more details.
The source code is available on: https://github.com/asweigart/pyautogui
PyAutoGUI has several features:Moving the mouse and clicking in the windows of other applications.
Sending keystrokes to applications (for example, to fill out forms).
Take screenshots, and given an image (for example, of a button or checkbox), and find it on the screen.
Locate an application’s window, and move, resize, maximize, minimize, or close it (Windows-only, currently).
Display alert and message boxes.''',interval=0.01)
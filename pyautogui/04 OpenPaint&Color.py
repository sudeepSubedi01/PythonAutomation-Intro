import pyautogui as pg
import time

# time.sleep(3)
# pg.moveTo(791,1079, duration=2)
# pg.leftClick(818,1041, duration=1)
# pg.typewrite('paint',interval=0.5)
# pg.leftClick(730,366, duration=1)
# pg.leftClick(1630,139, duration=1)
# pg.click(641,113)
pg.moveTo(419,334,duration=1)
pg.click()
time.sleep(3)
pg.dragRel(300,300,duration=1)
pg.click()
pg.moveTo()
print(pg.position())

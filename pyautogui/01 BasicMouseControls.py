import pyautogui as pg
import time

print(pg.size())
pg.moveTo(100,100,duration=1,tween=pg.easeInOutQuad)
pg.moveRel(0,50,duration=2)
print(pg.position())
pg.click(70,20,duration=1)
time.sleep(3)

# make a rectangle
pg.moveTo(960,540,duration=1)
pg.dragRel(0,50,duration=1)
pg.dragRel(50,0,duration=1)
pg.dragRel(0,-50,duration=1)
pg.dragRel(-50,0,duration=1)

# scroll
time.sleep(3)
pg.scroll(-500)
pg.scroll(200)
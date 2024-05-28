import pyautogui as pg

distance = 200
pg.moveTo(632,590,duration=1)
while distance > 0:
  pg.drag(distance,0,duration=0.5)
  distance -= 10
  pg.drag(0,distance,duration=0.5)
  distance -= 10
  pg.drag(-distance,0,duration=0.5)
  distance -= 10
  pg.drag(0,-distance,duration=0.5)
  distance -= 10


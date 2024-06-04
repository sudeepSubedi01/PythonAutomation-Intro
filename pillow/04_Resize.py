from PIL import Image
import os

for f in os.listdir('.'):
  if f.endswith('.jpeg'):
    i = Image.open(f)
    fname,fext = os.path.splitext(f)
    i.thumbnail((300,300))
    i.save('300size\\{}_300.png'.format(fname,fext))
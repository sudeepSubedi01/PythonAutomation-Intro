from PIL import Image
import os

for f in os.listdir('.'):
  if f.endswith('.jpeg'):
    i = Image.open(f)
    fn,fext = os.path.splitext(f)
    print(fn)
    print(fext)



# os.path.splitext(f) return a tuple of filename and its extension
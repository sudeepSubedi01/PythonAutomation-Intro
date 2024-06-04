from PIL import Image
import os

for f in os.listdir('.'):
  if f.endswith('.jpeg'):
    i = Image.open(f)
    fn,fext = os.path.splitext(f)
    # print(fn)
    i.save('pngs\\{}.png'.format(fn))


# the opened file is saved in a different location given in the .save method
# {} is replaced by fn
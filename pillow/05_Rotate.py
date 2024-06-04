from PIL import Image
import os

image1 = Image.open('bunny.jpeg')
image2 = image1.rotate(90)
fn,fext = os.path.splitext('bunny.jpeg')
print(fn)
print(fext)
# image1.show()
# image2.show()
image2.save('rotated\\{}_rotate.{}'.format(fn,fext))
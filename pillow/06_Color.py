from PIL import Image,ImageFilter

image1 = Image.open('dubai.jpeg')
image3 = image1.convert(mode = 'L')
image3.show()
image2 = image1.filter(ImageFilter.GaussianBlur(15))
image2.show()
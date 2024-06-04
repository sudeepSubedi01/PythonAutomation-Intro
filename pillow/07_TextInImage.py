from PIL import Image,ImageDraw,ImageFont

text = 'This is a cute bunny'
position = (130,502)
font= ImageFont.truetype('consola.ttf',36)

image1 = Image.open('bunny.jpeg')
draw = ImageDraw.Draw(image1)   # creating a drawing context for image1 instance
draw.text(position,text, (143,0,255), font = font)
image1.show()
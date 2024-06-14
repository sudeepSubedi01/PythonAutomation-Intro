import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import smtplib
from email.message import EmailMessage
import os

#text box info
textFieldHeight = 156
textFieldWidth = 947
textFieldX = 236
textFieldY = 997
textFieldCenterX = textFieldX + textFieldWidth//2
textFieldCenterY= textFieldY + textFieldHeight//2
font = ImageFont.truetype('AlexBrush-Regular.ttf',100)

#credentials
sender = '079bei042.sudeep@pcampus.edu.np'
password = 'electronics@#785'
subject = 'You are invited....'
body1 = 'Sample mail 3'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
print('Logged in!!!')

# position = (270,390)
data = pd.read_csv('sample.csv')
df = pd.DataFrame(data)
df['FullName'] = df['first_name'] +' '+ df['last_name']
nameList = df['FullName'].head().values
emailList = df['email'].head().values

for singleName, singleEmail in zip(nameList,emailList):
  card = Image.open('card.png')
  drawName = ImageDraw.Draw(card)
  singleName = str(singleName)
  singleEmail = str(singleEmail)
  # drawing in place
  bbox = drawName.textbbox((0, 0), singleName, font=font)
  text_width = bbox[2] - bbox[0]
  text_height = bbox[3] - bbox[1]
  name_x = textFieldCenterX - text_width // 2
  name_y = textFieldCenterY - text_height // 2
  drawName.text((name_x,name_y),singleName,fill=(244,189,24), font=font)
  # card.show()
  # print(singleName,singleEmail)
  # saving file
  temp_filename = f"welcome_{singleName.replace(' ', '_')}.png"
  card.save(temp_filename)

  # email message creation
  msg = EmailMessage()
  msg['From'] = sender
  msg['To'] = singleEmail
  msg['Subject'] = subject
  msg.set_content(body1)
    
  # attaching image to the email
  with open(temp_filename, 'rb') as img:
      img_data = img.read()
      img_name = os.path.basename(temp_filename)
      msg.add_attachment(img_data, maintype='image', subtype='png', filename=img_name)
    
  # sending email
  server.send_message(msg)
  print(f"Sent to: {singleName}")

  # deleting temporary file
  os.remove(temp_filename)

server.quit()
print('Server closed')
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import smtplib

sender = 'test@gmail.com'
password = 'test1'
# receiver = 'test2@gmail.com'
subject = 'Welcome to the Welcome program'
body1 = 'Hello we welcome you to the welcome party'

# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(sender,password)
# print('Logged in!!!')

position = (270,390)
font = ImageFont.truetype('consola.ttf',36)
data = pd.read_csv('contacts50.csv')
df = pd.DataFrame(data)
df['FullName'] = df['first_name'] +' '+ df['last_name']
nameList = df['FullName'].head().values
emailList = df['email'].head().values
for singleName, singleEmail in zip(nameList,emailList):
  print('looping')
  card = Image.open('card.jpeg')
  drawName = ImageDraw.Draw(card)
  drawName.text(position,singleName,(143,0,255),font = font)
  card.show()
  # ----------------------------------------------------------------------
  print(singleName,singleEmail)
  receiver = singleEmail
  # message = f'''From: Sender{sender}
  # To: receiver{singleEmail}
  # Subject: {subject}\n
  # {body1}'''
  # server.sendmail(sender,singleEmail,message)
  # print(f"Email sent successfully to {singleName}")
  

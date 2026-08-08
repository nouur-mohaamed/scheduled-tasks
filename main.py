import smtplib
import os
import dotenv
from email.message import EmailMessage
from datetime import datetime as dt
import random
today_date=dt.today()
to_email = "Salwa.maher@acg-eg.com"
from_email = "nouurmohaamed6777@gmail.com"
dotenv.load_dotenv()
password =str(os.getenv("PASSWORD"))
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=from_email,password=password)
    msg=EmailMessage()
    msg["from"]=from_email
    msg["to"]=to_email
    msg["subject"]="Salwa's everyday's Morning message"
    with open("message.txt") as file:
        morning_messages=file.readlines()
    msg.set_content(random.choice(morning_messages))
    connection.send_message(msg)
    

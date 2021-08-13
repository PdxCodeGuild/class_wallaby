import smtplib, ssl
import keys

def send_email(receiver_email, subject_str: str, body_str):


  port = 465
  smtp_server = "smtp.gmail.com"
  sender_email = keys.sender_email
  receiver_email = receiver_email
  password = keys.password
  ingredients = ''

  for item in body_str:
    ingredients += f'{item}\n'

  message = f"""\
Subject: {subject_str.title()} Ingredients

{ingredients}"""


  print(message)
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
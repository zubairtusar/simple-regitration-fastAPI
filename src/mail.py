import smtplib, ssl, secret

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = secret.sender_email
password = secret.password

def send_mail(receiver_email, reciever_name):
    message = f'Subject: Thank you for Registering!\n\nHello {reciever_name}\nHope you are having a great day! Thank you for registering in our application.\n\nKind Regards'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
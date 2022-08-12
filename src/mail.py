import smtplib, ssl, secret

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = secret.sender_email  # Enter your address
password = secret.password

def send_mail(receiver_email):
    message = f'Subject: Hello there {receiver_email.split("@")[0]}\n\nThis is a test mail sent using SMTPLib'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
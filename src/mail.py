import smtplib, ssl, secret

#configuration
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = secret.sender_email
password = secret.password

def send_mail(receiver_email, reciever_name):
    """Sends email to the provided receiver email.

    Args:
        receiver_email (str): email id to sent
        reciever_name (str): reciever name to add in the message
    """
    message = f'Subject: Thank you for Registering!\n\nHello {reciever_name}\nHope you are having a great day! Thank you for registering in our application.\n\nKind Regards'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
import bcrypt, mail, random, string

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

def verify_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

def send_welcome_mail(email):
    mail.send_mail(email)
    return True

def get_random_string(length=15):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

import bcrypt, mail, random, string
from email_validator import validate_email, EmailNotValidError

def get_hashed_password(salted_password):
    """_summary_

    Args:
        salted_password (str): salted_password

    Returns:
        (str): hashed password
    """
    return bcrypt.hashpw(salted_password.encode('utf-8'), bcrypt.gensalt())

def send_welcome_mail(email, user_name):
    """Sends email to the provided receiver email.

    Args:
        receiver_email (str): email id to sent
        reciever_name (str): reciever name to add in the message
    """
    mail.send_mail(email, user_name)

def get_random_string(length=15):
    """Generate salt

    Args:
        length (int, optional): Salt string length. Defaults to 15.

    Returns:
        (str): Salt string
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def validate_user_email(email):
    """Given an email, validates if the email format is valid and the domain exists

    Args:
        email (str): email to validate

    Returns:
        (bool, message): validated, error message
    """
    try:
        validate_email(email)
        return True, ''
    except EmailNotValidError as errorMsg:
        return False, str(errorMsg)

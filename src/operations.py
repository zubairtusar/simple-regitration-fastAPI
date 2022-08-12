import schemas, utils

def create_user(user: schemas.UserBase):
    hashed_password = utils.get_hashed_password(plain_text_password=user.password)

    return hashed_password

def send_welcome_mail(user: schemas.UserBase):
    pass
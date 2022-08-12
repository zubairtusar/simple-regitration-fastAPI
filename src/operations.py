import schemas, utils

def create_user(user: schemas.UserBase):
    hashed_password = utils.get_hashed_password(plain_text_password=user.password)
    print(f'[LOG] New user: {user.user_name} created with email: {user.email} and password {hashed_password}')
    return hashed_password
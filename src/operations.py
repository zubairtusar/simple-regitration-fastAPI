from sqlalchemy.orm import Session
import models, schemas, utils


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    salt = utils.get_random_string()
    hashed_password = utils.get_hashed_password(user.password + salt)
    db_user = models.User(user_name=user.user_name, email=user.email, hashed_password=hashed_password, salt=salt)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
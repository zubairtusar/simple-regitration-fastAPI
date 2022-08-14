from typing import List

from fastapi import FastAPI, Request, BackgroundTasks, HTTPException, Depends
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from database import SessionLocal, engine

import schemas, operations, utils, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory='template')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# For simple UI interactions 
# ------------------------------------------------------------------------------
@app.get("/")
def landing_page(request: Request):
    """Landing page, shows basic registration card

    Args:
        request (Request): request object

    Returns:
        templates.TemplateResponse(Jinja2Templates): html response
    """
    return templates.TemplateResponse('registrationPage.html', {
        "request": request,
    })

@app.get("/registered-users")
def registered_users(request: Request, db: Session = Depends(get_db)):
    """Shows all the registered users in a table

    Args:
        request (Request): request object
        db (Session, optional): database object | Defaults to Depends(get_db).

    Returns:
        templates.TemplateResponse(Jinja2Templates): html response
    """
    users = operations.get_users(db, skip=0, limit=100)

    return templates.TemplateResponse('usersPage.html', {
        "request": request,
        "users" : users
    })

# APIs
#------------------------------------------------------------------------------
@app.get('/users/', response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """_summary_

    Args:
        skip (int, optional): id to skip. Defaults to 0.
        limit (int, optional): Show user up to provided value. Defaults to 100.
        db (Session, optional): database object | Defaults to Depends(get_db).

    Returns:
        users(models.User): object of registered users
    """
    users = operations.get_users(db, skip=skip, limit=limit)
    return users

@app.post('/register/')
async def register_user(user: schemas.UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """_summary_

    Args:
        user (schemas.UserCreate): _description_
        background_tasks (BackgroundTasks): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Raises:
        HTTPException: if registered email tries to register again
        HTTPException: if provided email format is noit valid or the domain name is not valid

    Returns:
       (JSON): succss message
    """
    background_tasks.add_task(utils.send_welcome_mail, user.email, user.user_name)
    
    db_user = operations.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    validation, message = utils.validate_user_email(user.email)
    if validation:
        operations.create_user(db=db, user=user)
    else:
        raise HTTPException(status_code=401, detail=message)
    
    return {
        "code": "success",
        "message": f'{user.user_name}  successfully registered!'
    }

#uvicorn main:app --reload
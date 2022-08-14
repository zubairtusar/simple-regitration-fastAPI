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

@app.get("/")
def landing_page(request: Request):
    """Function to display landing page of the registration module

    Returns:
        _type_: _description_
    """
    return templates.TemplateResponse('registrationPage.html', {
        "request": request
    })

@app.get('/registered-users/', response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = operations.get_users(db, skip=skip, limit=limit)

    return users


@app.post('/register/')
async def register_user(user: schemas.UserCreate, request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    background_tasks.add_task(utils.send_welcome_mail, user.email, user.user_name)
    
    db_user = operations.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    return templates.TemplateResponse('landingPage.html', {
        "request": request
    })

#uvicorn main:app --reload
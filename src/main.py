from ast import operator
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import schemas, operations

app = FastAPI()
templates = Jinja2Templates(directory='template')

@app.get("/")
def landing_page(request: Request):
    """Function to display landing page of the registration module

    Returns:
        _type_: _description_
    """
    return templates.TemplateResponse('landingPage.html', {
        "request": request
    })


@app.post('/register/')
def create_user(user: schemas.UserBase):
    hashed_password = operations.create_user(user)
    print(f'[LOG] New user: {user.user_name} created with email: {user.email} and password {hashed_password}')
    return user

#uvicorn main:app --reload
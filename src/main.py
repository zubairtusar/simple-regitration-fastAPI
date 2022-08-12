from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates

import schemas, operations, utils

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
async def register_user(user: schemas.UserBase, background_tasks: BackgroundTasks):
    background_tasks.add_task(utils.send_welcome_mail, user.email)
    operations.create_user(user) 
    return user

#uvicorn main:app --reload
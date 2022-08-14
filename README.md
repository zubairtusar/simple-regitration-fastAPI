
# Registration Module using FastAPI and SQLAlchemy

## Description
The [repository](https://github.com/zubairtusar/simple-regitration-fastAPI) is an assignment for an interview process. This is a simple registration module that uses FastAPI and SQLAlchemy to register users and send them welcome mail.

## Installation
```
conda create -n env_name
pip install -r requirements.txt
```

## Configuration
* Go to ```/src``` directory:
```
cd src
```
* create secrets.py with your email and password to send mail from
```
sender_email = "example@example.com"  # Enter your email address
password = "example@123"  # Enter password
```

## Running
Run the following after activating the virtual enviornment.
```
uvicorn main:app --reload
```

## Authors
Zubair Rahman Tusar [@zubairtusar](https://github.com/zubairtusar)

## Acknowledgments
* [Codepen](https://codepen.io/sainthrax/pen/WwZxyB)
* [FastAPI Doc](https://fastapi.tiangolo.com/tutorial/sql-databases/)
* [Stock Screener Repository](https://github.com/hackingthemarkets/stockscreener)
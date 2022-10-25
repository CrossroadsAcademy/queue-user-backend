from urllib import response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import User,InputUser
from database import create_user, get_all_user

app = FastAPI()



origin = "http://localhost:3000/"

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials =True,
    allow_methods = ['*'],
    allow_headers = ['*']

)


@app.post('/signup')
async def create_user_view(user:InputUser):
    response = await create_user(user)
    return response

@app.get('/all_user')
async def all_user():
    response = await get_all_user()
    return response
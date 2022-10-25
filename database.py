from http import client
from ipaddress import collapse_addresses
from multiprocessing.sharedctypes import Value
from typing import Collection
from passlib.hash import pbkdf2_sha256
from model import User,InputUser
import motor.motor_asyncio 
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://Hacktober-project:ACuEq8UJWfkzIuwE@project-queue.kdzeir1.mongodb.net/?retryWrites=true&w=majority')


database = client.User

collection = database.user

async def create_user(user):
    user = user.dict()
    user_instance = User(**user,staff = True,status=True)
    hash = pbkdf2_sha256.hash(user_instance.password)
    user_instance.password = hash
    document = user_instance.dict()
    print(document)


    result = await collection.insert_one(document)
    return True

async def get_all_user():
    user = []
    cursor = collection.find({})
    async for document in cursor:
        print(document)
        if document['username'] == 'sai':
            ob = User(**document)
            user.append(ob)
            print(ob.user_return())
            username, emai, password = ob.user_return()
            print(password)
            if pbkdf2_sha256.verify('sais',password):
                print('sai authenticated')
    return True
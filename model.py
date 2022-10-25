import email
from pydantic import BaseModel





class InputUser(BaseModel):
    username:str
    password:str
    email:str
    


class User(BaseModel):
    username:str
    password:str
    email:str
    staff:bool
    status:bool

    def user_return(self):
        return self.username,self.email,self.password


from pydantic import BaseModel
from typing import Optional
import datetime


class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class TweetBase(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class ShowTweet(BaseModel):
    id: int
    created: Optional[datetime.datetime]
    title: str
    description: str
    user_id: int

    user: ShowUser

    class Config:
        orm_mode = True

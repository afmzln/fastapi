from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base
import datetime
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    tweet = relationship("Tweet", back_populates="user")

class Tweet(Base):
    __tablename__ = "tweet"
    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tweet")
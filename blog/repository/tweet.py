from sqlalchemy.orm import Session
from .. import models, schemas, token
from fastapi import HTTPException, status


def get_all(db: Session):
    tweets = db.query(models.Tweet).all()
    return tweets


def create(request: schemas.TweetBase, db: Session,  user_id: int):
    new_tweet = models.Tweet(title=request.title, description=request.description, user_id=user_id)
    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)
    return new_tweet


def show(id: int, db: Session):
    tweet = db.query(models.Tweet).filter(models.Tweet.id == id).first()
    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tweet with the id {id} is not available")
    return tweet


def delete(id: int, db: Session):
    db.query(models.Tweet).filter(models.Tweet.id == id)
    tweet = db.query(models.Tweet).filter(models.Tweet.id == id)
    if not tweet.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tweet with id {id} not found")
    tweet.delete(synchronize_session=False)
    db.commit()
    return "done"

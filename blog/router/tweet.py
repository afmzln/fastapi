from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models, oauth2, token
from sqlalchemy.orm import Session
from ..repository import tweet, user
get_db = database.get_db

router = APIRouter(
    prefix="/tweet",
    tags=["Tweet"]
)


# GET ALL tweets
@router.get("/", response_model=List[schemas.ShowTweet])
def all_tweet(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tweet.get_all(db)


# CREATE tweet
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_tweet(id: int, request: schemas.TweetBase, db: Session = Depends(get_db),
                 current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tweet.create(request, db, user_id=id)



# DELETE tweet
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tweet(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return tweet.delete(id, db)

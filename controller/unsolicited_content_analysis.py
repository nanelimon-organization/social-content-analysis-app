from sqlalchemy import func, desc, or_, text, and_, tuple_
from models import twitter
from flask_sqlalchemy import SQLAlchemy
"""

db = SQLAlchemy()


def get_all_tweets():
    tweets = db.session.query(twitter.Tweet).all()
    #tweets = twitter.Tweet.query.all()
    return tweets"""
from models import twitter
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_all_tweets():
    tweets = twitter.Tweet.query.all()
    return tweets

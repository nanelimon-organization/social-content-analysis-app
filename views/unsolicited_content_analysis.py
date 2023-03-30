from flask import render_template, jsonify, redirect, Blueprint, flash
import pytz
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from models.twitter import Tweet
from controller import unsolicited_content_analysis

uns_cont_alys = Blueprint('uns_cont_alys', __name__,
    template_folder='templates',
    static_folder='static')

db = SQLAlchemy()


@uns_cont_alys.route('/', methods=['GET'])
def index():

    tweets = unsolicited_content_analysis.get_all_tweets()

    local_tz = pytz.timezone('Europe/Istanbul')  # yerel zaman dilimi olarak burada İstanbul kullanıldı

    sorted_tweets = sorted(tweets, key=lambda x: x.id, reverse=True)

    for tweet in sorted_tweets:
        print(tweet.id)
        print(tweet.device)
        print(tweet.tweet_url)
        print(tweet.publish_date)
        print(tweet.user_location)


    hashtags= ['turkcell', 'turktelekom']
    username='@KullanıcıAdı'
    publish_date= '2023-03-26T21:18:11+00:00'

    return render_template('index.html', hashtags=hashtags,
                           username=username,publish_date=publish_date, tweets=sorted_tweets)

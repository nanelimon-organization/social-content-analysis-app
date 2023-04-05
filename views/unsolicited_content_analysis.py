import json
import requests
from flask import render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from controller import unsolicited_content_analysis

uns_cont_alys = Blueprint('uns_cont_alys', __name__,
    template_folder='templates',
    static_folder='static')

db = SQLAlchemy()


@uns_cont_alys.route('/', methods=['GET'])
def index():
    tweets = unsolicited_content_analysis.get_all_tweets()
    sorted_tweets = sorted(tweets, key=lambda x: x.id, reverse=True)

    contents = [i.content for i in sorted_tweets]
    predict = model_sequence(tweets=contents)

    return render_template('index.html', tweets=sorted_tweets, predict=predict)


def model_sequence(tweets):

    api_url = "http://127.0.0.1:5001/multilabel-prediction"
    items = json.dumps({"texts": tweets})
    response = requests.post(api_url, items)
    results = response.json()["result"]["model"]

    return results

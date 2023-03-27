from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    hashtags= ['turkcell', 'turktelekom']
    username='@KullanıcıAdı'
    publish_date= '2023-03-26T21:18:11+00:00'

    return render_template('index.html', hashtags=hashtags, tarih=datetime.date.today(), username=username,publish_date=publish_date)


if __name__ == '__main__':
    app.run(port=8000)

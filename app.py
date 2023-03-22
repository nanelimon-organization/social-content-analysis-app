from flask import Flask
from flask import render_template
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    text = '@KullanıcıAdı - hhtps://twitter.com/usr_url_adres'
    return render_template('index.html', text=text, tarih=datetime.date.today())


if __name__ == '__main__':
    app.run(port=8000)

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from views.unsolicited_content_analysis import uns_cont_alys
from views import unsolicited_content_analysis
from decouple import config

app = Flask(__name__)

# Load environment variables
db_user = config('USERNAME')
db_pass = config('PASSWORD')
db_host = config('HOST')
db_port = config('PORT')
db_name = config('DATABASE')

# Set SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SESSION_TYPE'] = 'filesystem'
#Session(app)

# Initialize SQLAlchemy instance
db = SQLAlchemy(app)

app.register_blueprint(uns_cont_alys)
app.secret_key = b'acikhack2023tddi'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

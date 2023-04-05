from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tweet(db.Model):
    __tablename__ = 'tweets'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))
    tweet_url = db.Column(db.String(255), unique=True, nullable=False)
    user_url = db.Column(db.String(255))
    user_location = db.Column(db.String(255))
    username = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    publish_date = db.Column(db.String(255))
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    hashtags = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Tweet {self.username}>'

    def __set_name__(self, owner, name):
        return f'owner: {self.owner} - name: {self.name}'

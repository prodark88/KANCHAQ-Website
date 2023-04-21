
from blogr import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200), default=None)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"


from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    url = db.Column(db.String(200), nullable=False, unique=True)
    title = db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    #author = db.relationship('users', backref=db.backref('posts', lazy=True))
    author = db.relationship(User, backref=db.backref('posts', lazy=True))


    def __init__(self, author, url, title, info, content):
        self.author = author
        self.url = url
        self.title = title
        self.info = info
        self.content = content
    def __repr__(self):
        return f"Post(id={self.id}, author_id={self.author_id}, title='{self.title}', url='{self.url}')"





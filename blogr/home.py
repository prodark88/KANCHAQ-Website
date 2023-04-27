from flask import Blueprint, render_template, redirect, url_for, request, g , session , flash

bp=Blueprint('home', __name__)


from .models import User, Post
from blogr import db


def get_user(id):
    user=User.query.get_or_404(id)
    return user

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, get_user = get_user)


@bp.route('/blog/<url>')
def blog(url):
    post = Post.query.filter_by(url = url).first()
    return render_template('blog.html',post=post, get_user=get_user)

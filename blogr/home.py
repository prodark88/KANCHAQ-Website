from flask import Blueprint, render_template, redirect, url_for, request, g , session , flash

bp=Blueprint('home', __name__)


from .models import User, Post
from blogr import db



@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/blog')
def blog():
    return render_template('blog.html')

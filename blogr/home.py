from flask import Blueprint, render_template, redirect, url_for

bp=Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/blog')
def blog():
    return render_template('blog.html')

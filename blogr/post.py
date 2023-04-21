from flask import Blueprint, render_template, redirect, url_for

bp=Blueprint('post', __name__, url_prefix='/post')

@bp.route('/posts')
def posts():
    return render_template('post/post.html')


@bp.route('/create')
def create():
    return render_template('post/create.html')

@bp.route('/update')
def update():
    return render_template('post/update.html')

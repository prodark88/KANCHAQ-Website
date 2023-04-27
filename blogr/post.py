from flask import Blueprint, render_template, redirect, url_for, request, g , session , flash

from .models import Post
from blogr import db
from .auth import login_required



bp=Blueprint('post', __name__, url_prefix='/post')

#mostrar los post del usuario
@bp.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    return render_template('admin/post.html',posts= posts)

#crear post por usuario logeado
@bp.route('/create',methods=['POST', 'GET'])
@login_required
def create():
    if request.method == 'POST':
        url = request.form.get('url')
        url = url.replace(' ','-')
        title = request.form.get('title')
        info = request.form.get('info')
        content = request.form.get('ckeditor')


        post = Post(g.user.id, url, title, info, content)

        msj_error = None
        
        post_url=Post.query.filter_by(url=url).first()
        if post_url == None:
            db.session.add(post)
            db.session.commit()
            flash(f'el blog {post.title} se registro correctamente')
            return redirect(url_for('post.posts'))
        else:
            msj_error = f'El URL {url} ya esta registrado'
            flash(msj_error)

    return render_template('admin/create.html',)

@bp.route('/update/<int:id>',methods=['POST', 'GET'])
@login_required
def update(id):
    post = Post.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form.get['title']
        post.info = request.form.get['info']
        post.content = request.form.get['ckeditor']

        db.session.commit()
        flash(f'El blog {post.title} se actualizo correctamente')
        return redirect(url_for('post.posts'))   
     
    return render_template('admin/update.html', post=post)





@bp.route('/delete/<int:id>',methods=['POST', 'GET'])
@login_required
def delete(id):
    post= Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash(f'El blog {post.title} se elimino correctamente')

    return redirect(url_for('post.posts'))




from flask import Blueprint, render_template, redirect, url_for

bp=Blueprint('auth', __name__, url_prefix='/auth')


#Resgitrar usuarios
@bp.route('/register')
def register():
    return render_template('auth/regiser.html')

#Accceder a la pagina 
@bp.route('/login')
def login():
    return render_template('auth/login.html')


#Accerder al perfil
@bp.route('/profile')
def profile():
    return render_template('auth/profile.html')

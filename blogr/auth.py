from flask import Blueprint, render_template, redirect, url_for, request, g , session , flash, abort

# para la seguridad
from werkzeug.security import generate_password_hash, check_password_hash


#para trabajr el login
from flask_login import current_user, login_user 
from .forms import LoginForm



bp=Blueprint('auth', __name__, url_prefix='/auth')


#base y clase necesaria para trabajar en el auth
from .models import User
from blogr import db
#Resgitrar usuarios
@bp.route('/register', methods =['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Obtener los valores del formulario
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password= request.form['confirm_password']

        # Verificar si las contraseñas coinciden
        if password != confirm_password:
            flash('Las contraseñas no coinciden.')
            return redirect(url_for('auth.register'))

        # Generar el hash de la contraseña
        hashed_password = generate_password_hash(password)


        user = User.query.filter_by(username=username).first()
        if user is not None:
            flash('El nombre de usuario ya esta en uso.')
            return redirect(url_for('auth.register'))
        
        # Guardar el usuario en la base de datos
        user = User(username=username, email=email, password=hashed_password)
        setattr(user, 'password', hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Registro exitoso, Por FAVOR , Inicie sesion.')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html')


#Accceder a la pagina 
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los valores del formulario
        
        email = request.form['email']
        password = request.form['password']
        


        error = None
        user = User.query.filter( User.email == email).first()
        
        if user ==  None or not check_password_hash(user.password, password):
            error = 'Correo o contraseña es incorrecta'

        if error is None:
            session.clear()
            session['user_id']=user.id
            return redirect(url_for('post.posts'))
        
        flash(error)

    return render_template('auth/login.html')
'''
#mantener inicio de sesion
@bp.before_app_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])
'''

#decorador para colocar en vistas
import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.logout'))
        return view(**kwargs)
    return wrapped_view

#decorador para mantener sesion
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is not None:
        g.user = User.query.get(user_id)
    else:
        pass #abort(404)
        

#cerrar sesion
@bp.route('/logout')
def logout():
    if  g.user:
        session.clear()
    flash('Sesión cerrada correctamente.')
    return redirect(url_for('home.index'))


#Accerder al perfil
@bp.route('/profile')
@login_required

def profile():
    return render_template('auth/profile.html')
from flask import Blueprint, render_template, redirect, url_for, request, g , session , flash

# para la seguridad
from werkzeug.security import generate_password_hash, check_password_hash



from flask_login import current_user, login_user 
from werkzeug.security import check_password_hash

from .forms import LoginForm





bp=Blueprint('auth', __name__, url_prefix='/auth')


#base y clase necesaria para trabajar en el auth
from .models import db , User

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
    # Si el usuario ya está autenticado, redirigirlo a la página de inicio
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    # Crear un objeto del formulario de inicio de sesión
    form = LoginForm()

    if form.validate_on_submit():
        # Buscar el usuario por nombre de usuario o correo electrónico
        user = User.query.filter_by(username=form.username_or_email.data).first() \
            or User.query.filter_by(email=form.username_or_email.data).first()

        # Verificar si el usuario existe y si la contraseña es correcta
        if user and check_password_hash(user.password, form.password.data):
            # Iniciar sesión al usuario
            login_user(user, remember=form.remember_me.data)
            flash('Ha iniciado sesión correctamente.')
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('Usuario o contraseña incorrectos.')

    return render_template('auth/login.html', form=form)


#Accerder al perfil
@bp.route('/profile')
def profile():
    return render_template('auth/profile.html')

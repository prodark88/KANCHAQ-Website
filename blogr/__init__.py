from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    #CREAR LA APP
    app=Flask(__name__)



    app.config.from_object('config.Config')
    db.init_app(app)
    






    # Registro de vistas

    from blogr import home #registro del inicio de pagina
    app.register_blueprint(home.bp)

    from blogr import auth # registro de la pagina de autenticacion
    app.register_blueprint(auth.bp)

    from blogr import post #registro de la pagina de post
    app.register_blueprint(post.bp)


    #migrar nuestro modelos de manera automatica a nuesta BB.DD
    from .models import User, Post
    with app.app_context():
        db.create_all()

    return app
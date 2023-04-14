from flask import Flask

def create_app():
    #CREAR LA APP
    app=Flask(__name__)
    






    # Registro de vistas

    from blogr import home #registro del inicio de pagina
    app.register_blueprint(home.bp)

    from blogr import auth # registro de la pagina de autenticacion
    app.register_blueprint(auth.bp)

    from blogr import post #registro de la pagina de post
    app.register_blueprint(post.bp)

    return app
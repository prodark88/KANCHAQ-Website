from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    # Crear la aplicación
    app = Flask(__name__)

    # Configurar la aplicación
    app.config.from_object('config.Config')

    # Inicializar las extensiones
    db.init_app(app)
    migrate = Migrate(app, db)

    # Registrar las vistas
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import post
    app.register_blueprint(post.bp)

    return app

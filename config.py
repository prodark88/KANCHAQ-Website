
POSTGRESQL ='postgresql://postgres:elmiocid789mio@localhost:5432/blogspost_db'


SQLITE = 'sqlite:///blogspost_db.sqlite'
class Config:
        DEBUG = True
        SECRET_KEY = 'dev'

        
        SQLALCHEMY_DATABASE_URI = SQLITE
        SQLALCHEMY_TRACK_MODIFICATIONS = False
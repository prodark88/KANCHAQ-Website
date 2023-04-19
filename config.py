SQLITE = ''
POSTGRESQL ='postgresql://postgres:elmiocid789mio@localhost:5432/blogspost_db'




class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
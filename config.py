SQLITE = 'sqlite:///project.db'
POSTGRESQL = 'postgresql+psycopg2://postgres:postgres@localhost:5432/blogposts_db'



class Config:
    SERVER_NAME="127.0.0.1:80"
    DEBUG = True    
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = SQLITE
    CKEDITOR_PKG_TYPE = 'full'
    
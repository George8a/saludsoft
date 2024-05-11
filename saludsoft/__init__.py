from flask import Flask, render_template, request, flash, url_for, redirect, session, g

from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    
    #configuracion del proyecto
    app.config.from_object('config.Config')
   
    db.init_app(app)
    
    #registrar las vistas
    from saludsoft import auth
    app.register_blueprint(auth.bp)
    
                      
        
    # @app.route('/', methods=['GET'])
    # def index():
        
       
    #     return render_template('index.html')
    
    
    from .models import User
    with app.app_context():
        db.create_all()
    
    
    return app
from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from saludsoft import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


import functools
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**Kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**Kwargs)
    return wrapped_view



@bp.route('register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        
        user = User(username, email, generate_password_hash(password))
        #validacion de datos
        error = None
        user_email = User.query.filter_by(email = email).first()
        
        if user_email == None:
            db.session.add(user)
            db.session.commit()
            error = f'Se creo el usuario correctamente {username}, contactar al Administrador para activar el usuario'
            
            
        else:
            error = f'el correo {email} ya se encuentra registrado'
        
        flash(error)
    return render_template('auth/register.html')



def ingresar(password, email): 

    
    email = email
    password = password
                
                #validaciones de datos
    error = None
    user = User.query.filter_by(email = email).first()
                
    if user == None or not check_password_hash(user.password, password):
                    
        error = 'correo o contraseña incorrecta'
    elif user.estado == False:
            
       error = 'El usuario se encuentra inactivo, validar con el administrador'                        
    elif error is None:
        
        
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for('auth.menu'))
        #print('ingreso exitoso')
    flash(error)
    return render_template('index.html')


@bp.route('/menu')
@login_required
def menu():
    return render_template('auth/menu.html')



@bp.route('/adminusuario')
@login_required
def adminUsuario():
    return render_template('auth/admin.html')
            
    
        







@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)
        
        

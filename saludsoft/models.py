from saludsoft import db

class User(db.Model):
    __tablename__= 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Text, nullable=False)
    estado = db.Column(db.Boolean, default=False)
    
    
    def __init__(self, username, email, passsword, estado = False):
        self.username = username
        self.email = email
        self.password = passsword
        self.estado = estado
        
        
    def __repr__(self):
        return f"User:{self.username}"
    
    

    
    
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    nome = db.Column(db.String(64), nullable=False)
    sobrenome = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nacionalidade = db.Column(db.String(64), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    estado = db.Column(db.String(64), nullable=False)
    cidade = db.Column(db.String(64), nullable=False)
    logradouro = db.Column(db.String(128), nullable=False)
    telefone = db.Column(db.String(14), nullable=False)

    @property
    def is_authenticated(self):
        return True
        
    @property
    def is_active(self):
        return True    
        
    @property
    def is_anonymous(self):
        return False 
        
    def get_id(self):
        return self.id

    def __init__(self, username, password, email, nome, sobrenome,
                 cpf, nacionalidade, cep, estado, cidade, logradouro, telefone):
        self.username = username
        self.password = password
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.nacionalidade = nacionalidade
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.logradouro = logradouro
        self.telefone = telefone

    def __repr__(self):
        return "<User %r>" %self.username

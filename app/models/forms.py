from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SelectField, validators

class LoginForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()])
    password = PasswordField("password", [validators.DataRequired()])

class SingupForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()])
    password = PasswordField("password", [validators.DataRequired()])
    confirm = PasswordField("confirm", [validators.DataRequired()])
    email = StringField("email", [validators.DataRequired()])
    nome = StringField("nome", [validators.DataRequired()])
    sobrenome = StringField("sobrenome", [validators.DataRequired()])
    cpf = StringField("cpf", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$'), validators.Length(min=14, max=14)])
    nacionalidade = StringField("nacionalidade", [validators.DataRequired()])
    cep = StringField("cep", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$'), validators.Length(min=9, max=9)])
    estado = StringField("estado", [validators.DataRequired()])
    cidade = StringField("cidade", [validators.DataRequired()])
    logradouro = StringField("logradouro", [validators.DataRequired()])
    telefone = StringField("telefone", [validators.DataRequired(), validators.Regexp('^[0-9-.()+]+$')])

class EditForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()])
    email = StringField("email", [validators.DataRequired()])
    nome = StringField("nome", [validators.DataRequired()])
    sobrenome = StringField("sobrenome", [validators.DataRequired()])
    cpf = StringField("cpf", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$'), validators.Length(min=14, max=14)])
    nacionalidade = StringField("nacionalidade", [validators.DataRequired()])
    cep = StringField("cep", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$'), validators.Length(min=9, max=9)])
    estado = StringField("estado", [validators.DataRequired()])
    cidade = StringField("cidade", [validators.DataRequired()])
    logradouro = StringField("logradouro", [validators.DataRequired()])
    telefone = StringField("telefone", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$')])

class EditMeForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()])
    password = PasswordField("password")
    newpassword = PasswordField("newpassword")
    email = StringField("email", [validators.DataRequired()])
    nome = StringField("nome", [validators.DataRequired()])
    sobrenome = StringField("sobrenome", [validators.DataRequired()])
    cpf = StringField("cpf", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$'), validators.Length(min=14, max=14)])
    nacionalidade = StringField("nacionalidade", [validators.DataRequired()])
    cep = StringField("cep", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$'), validators.Length(min=9, max=9)])
    estado = StringField("estado", [validators.DataRequired()])
    cidade = StringField("cidade", [validators.DataRequired()])
    logradouro = StringField("logradouro", [validators.DataRequired()])
    telefone = StringField("telefone", [validators.DataRequired(), validators.Regexp('^[0-9-.]+$')])
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db, lm
from app.models.tables import User
from app.models.forms import LoginForm, SingupForm, EditForm, EditMeForm

@lm.user_loader
def get_user(user_id):    
    return User.query.get(int(user_id))

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    users = User.query.all()
    return render_template('dashboard.html', users=users)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Logado com sucesso")
                return redirect(url_for("index"))
            else:
                flash("Senha incorreta")
                return redirect(url_for("login"))
        else:
            flash("Login inválido")
    return render_template('login.html', form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/cadastre-se", methods=["GET", "POST"])
def cadastrar():
    form = SingupForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=generate_password_hash(form.password.data), email=form.email.data, nome=form.nome.data, sobrenome=form.sobrenome.data, cpf=form.cpf.data, nacionalidade=form.nacionalidade.data, cep=form.cep.data, estado=form.estado.data, cidade=form.cidade.data, logradouro=form.logradouro.data, telefone=form.telefone.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Usuário cadastrado, efetue o login")
        return redirect(url_for("login"))
    else:
        for error in form.errors:
            flash("O " + error + " é invalido", )
    return render_template('cadastre-se.html', form=form)

@app.route("/deletar/<int:id>", methods=["GET", "DELETE"])
@login_required
def deletar(id):
    user_to_delete = User.query.get_or_404(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    flash("O usuário " +user_to_delete.username+ " foi excluído")
    return redirect(url_for("dashboard"))

@app.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    user_to_edit = User.query.filter_by(id=id).first()
    if user_to_edit.id == current_user.id:
        form = EditMeForm()
    else:
        form = EditForm()

    if form.validate_on_submit():
        if form == EditMeForm():
            if form.newpassword.data is not None:
                if check_password_hash(user_to_edit.password, form.password.data):
                    user_to_edit.username = form.username.data
                    user_to_edit.password = generate_password_hash(form.newpassword.data)
                    user_to_edit.nome = form.nome.data
                    user_to_edit.sobrenome = form.sobrenome.data
                    user_to_edit.email = form.email.data
                    user_to_edit.telefone = form.telefone.data
                    user_to_edit.cpf = form.cpf.data
                    user_to_edit.nacionalidade = form.nacionalidade.data
                    user_to_edit.cep = form.cep.data
                    user_to_edit.estado = form.estado.data
                    user_to_edit.cidade = form.cidade.data
                    user_to_edit.logradouro = form.logradouro.data
                    db.session.add(user_to_edit)
                    db.session.flush()
                    db.session.commit()
                    flash("Os dados foram alterados")
                    return redirect(url_for("dashboard"))
                else:
                    flash("Senha incorreta")
                    return redirect(url_for("editar", id=user_to_edit.id))

        else:
            user_to_edit.username = form.username.data
            user_to_edit.nome = form.nome.data
            user_to_edit.sobrenome = form.sobrenome.data
            user_to_edit.email = form.email.data
            user_to_edit.telefone = form.telefone.data
            user_to_edit.cpf = form.cpf.data
            user_to_edit.nacionalidade = form.nacionalidade.data
            user_to_edit.cep = form.cep.data
            user_to_edit.estado = form.estado.data
            user_to_edit.cidade = form.cidade.data
            user_to_edit.logradouro = form.logradouro.data
            db.session.add(user_to_edit)
            db.session.flush()
            db.session.commit()
            flash("Os dados foram alterados")
            return redirect(url_for("dashboard"))

    form.username.data = user_to_edit.username
    form.nome.data = user_to_edit.nome
    form.sobrenome.data = user_to_edit.sobrenome
    form.email.data = user_to_edit.email
    form.telefone.data = user_to_edit.telefone
    form.cpf.data = user_to_edit.cpf
    form.nacionalidade.data = user_to_edit.nacionalidade
    form.cep.data = user_to_edit.cep
    form.estado.data = user_to_edit.estado
    form.cidade.data = user_to_edit.cidade
    form.logradouro.data = user_to_edit.logradouro
    return render_template('editar.html', form=form, user=id)

@app.route("/consultar/<int:id>", methods=["GET","POST"])
@login_required
def consultar(id):
    user = User.query.get_or_404(id)
    return jsonify({"id": user.id,
                    "username": user.username,
                    "nome": user.nome,
                    "sobrenome": user.sobrenome,
                    "email": user.email,
                    "telefone": user.telefone,
                    "cpf": user.cpf,
                    "nacionalidade": user.nacionalidade,
                    "cep": user.cep,
                    "estado": user.estado,
                    "cidade": user.cidade,
                    "logradouro": user.logradouro})

@app.route("/inserir", methods=["GET","POST"])
@login_required
def inserir():
    form = SingupForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=generate_password_hash(form.password.data), email=form.email.data, nome=form.nome.data, sobrenome=form.sobrenome.data, cpf=form.cpf.data, nacionalidade=form.nacionalidade.data, cep=form.cep.data, estado=form.estado.data, cidade=form.cidade.data, logradouro=form.logradouro.data, telefone=form.telefone.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Usuário cadastrado")
        return redirect(url_for("dashboard"))
    else:
        for error in form.errors:
            flash("O " + error + " é invalido", )
    return render_template('inserir.html', form=form)

@app.route("/remover", methods=["GET","POST"])
@login_required
def remover():
    users = User.query.all()
    return render_template('remover.html', users=users)

@app.route("/alterar", methods=["GET","POST"])
@login_required
def alterar():
    users = User.query.all()
    return render_template('alterar.html', users=users)
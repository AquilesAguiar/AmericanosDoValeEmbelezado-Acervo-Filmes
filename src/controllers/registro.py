from flask import render_template,redirect,request,redirect,flash,url_for
from models.usuarios import *

def index():
    return render_template('registro.html')

def cadastro():
    nome = request.form['Nome']
    email = request.form['Email']
    senha = request.form['Senha']
    ctrlUser = adicionarUser(nome,email,senha)

    if ctrlUser == True:
        return redirect(url_for("login.index"))

    flash('Este email já está sendo utilizado')
    return redirect(url_for("registro.registro"))
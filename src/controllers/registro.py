from flask import render_template,redirect,request,redirect,flash,url_for
from models.usuarios import *

def index():
    return render_template('registro.html')

def cadastro():
    nome = request.form['Nome']
    idade = request.form['Idade']
    email = request.form['Email']
    senha = request.form['Senha']
    perfilUsuario = request.form['perfilUsuario']
    ctrlUser = adicionarUser(nome,idade,email,senha,perfilUsuario)

    if ctrlUser == True:
        return redirect(url_for("login.index"))

    flash('Este email já está sendo utilizado')
    return redirect(url_for("registro.registro"))
from flask import render_template,redirect,request,redirect,flash,url_for
from models.usuarios import *


def index():
    return render_template('logar.html',)

def logar():
    email = request.form['Email']
    senha = request.form['Senha']
    ctrlUser = logarUsuario(email,senha)

    if ctrlUser == True:
        user = dadosUser(email,senha)
        return redirect(url_for("principal.index"))

    flash('Email ou senha errados')
    return redirect(url_for('login.index'))
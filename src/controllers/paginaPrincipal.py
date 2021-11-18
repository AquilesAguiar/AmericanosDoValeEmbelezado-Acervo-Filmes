from flask import render_template,redirect,request,redirect,flash,url_for
from models.filmes import filmes
from pprint import pprint

Filmes = filmes()
def index():    
    return render_template('index.html',emCartaz=Filmes.getFilmesEmCartaz())

def pesqFilmes():
    filmePesq = request.get_json()
    print(filmePesq)
    return render_template('infoFilmes.html',Filmes=Filmes.getFilmes(filmePesq))

from flask import render_template,redirect,request,redirect,flash,url_for
from models.filmes import filmes
from  models.aluguelFilmes import *
from pprint import pprint
from random import uniform

Filmes = filmes()
def index():    
    return render_template('index.html',emCartaz=Filmes.getFilmesEmCartaz())

def pesqFilmes():
    filmePesq = request.args.get('filme')
    FilmesCl = Filmes.getFilmes(filmePesq)
    if FilmesCl == []:
        return render_template("pageError.html")
    FilmesRecomend = Filmes.getRecomendacao(FilmesCl[0]['id'])
    return render_template('infoFilmes.html',Filmes=FilmesCl,FilmesRecomend=FilmesRecomend)

def alugar():
    preco = round(uniform(20.00,99.99),2)
    filmeAluguel = request.args.get('filme')
    FilmesCl = Filmes.getFilmeID(filmeAluguel)
    return render_template("alugar.html",filme=FilmesCl,preco=preco)

def finalizarAluguel():
    dadosAluguel = request.get_json()
    nome = Filmes.getFilmeID(dadosAluguel['id'])["title"]
    adicionarFilme(dadosAluguel['id'],nome)
    return {'success': True}

def graficoFilmes():
    return retornaFilmesGrafico()
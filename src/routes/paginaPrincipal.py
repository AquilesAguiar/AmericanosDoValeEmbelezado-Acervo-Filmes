from flask import Blueprint
from controllers.paginaPrincipal import *

principal = Blueprint("principal",__name__)

principal.route('/',methods=['GET'])(index)
principal.route('/pesquisa',methods=['GET'])(pesqFilmes)
principal.route('/alugar',methods=['GET'])(alugar)
principal.route('/finalizarAlugar',methods=['POST'])(finalizarAluguel)
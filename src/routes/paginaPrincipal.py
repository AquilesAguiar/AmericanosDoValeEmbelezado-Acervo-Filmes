from flask import Blueprint
from controllers.paginaPrincipal import *

principal = Blueprint("principal",__name__)

principal.route('/',methods=['GET'])(index)
principal.route('/pesquisa',methods=['POST'])(pesqFilmes)
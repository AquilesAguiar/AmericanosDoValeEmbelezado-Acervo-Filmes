from flask import Blueprint
from controllers.registro import *

registro = Blueprint('registro',__name__)

registro.route('/',methods=['GET'])(index)

registro.route('/cadastrar',methods=["POST"])(cadastro)
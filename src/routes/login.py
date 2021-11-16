from flask import Blueprint
from controllers.login import *

login = Blueprint('login',__name__)

login.route('/',methods=['GET'])(index)

login.route('/logar',methods=["POST"])(logar)
from flask import Flask
import os
from routes.login import login
from routes.registro import registro
from routes.paginaPrincipal import principal

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

app.register_blueprint(login,url_prefix='/')
app.register_blueprint(registro,url_prefix='/registro')
app.register_blueprint(principal,url_prefix='/filmes')

if __name__ == '__main__':
    app.run(debug=True,port=8787)
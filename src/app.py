from flask import Flask
import os
from routes.login import login
from routes.registro import registro

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

app.register_blueprint(login,url_prefix='/')
app.register_blueprint(registro,url_prefix='/registro')

if __name__ == '__main__':
    app.run(debug=True,port=8787)
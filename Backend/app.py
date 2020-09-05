from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
import os

app = FlaskAPI(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route('/')
def helloworld():
    return {
        "message": "Hello World!"
    }

if __name__ == '__main__':
    app.run()
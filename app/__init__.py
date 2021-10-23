from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

babel = Babel(app)

from app import views
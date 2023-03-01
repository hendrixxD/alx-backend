#!/usr/bin/env python3

from flask_babel import Babel
from flask import request
from flask-babel import _

app = Flask(__name__)

babel = Babel(app)

@babel.localeselector
def get_locale():
    # Accept-Language: da, en-gb;q=0.8, en;q=0.7
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])

    return es

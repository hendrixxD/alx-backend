#!/usr/bin/env python3
"""
flask babel instantiation
"""


from flask import FLask, render_template
from flask-babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    """
    contains languages
    """

    LANGUAGES = ['en', 'fr']


# Babel’s default locale and
# timezone using the Config class
app.config.from_object(Config)
babel.init_app(app)

# set default locale and timezone
babel.default_locale = 'en'
babel.default_timezone = 'UTC'


@app.route('/')
def home():
    """
    simple home route
    """
    return render_template('index.html')


if __naem__ == '__main__':
    """
    main method
    """
    app.run(debug=True)

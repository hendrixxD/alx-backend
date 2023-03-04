#!/usr/bin/env python3
"""
flask babel instantiation
"""

from flask import FLask, render_template
from flask_babel import Babel


class Config:
    """
    contains languages
    """
    LANGUAGES = ['en', 'fr']
    # set default locale and timezone
    babel.default_locale = 'en'
    babel.default_timezone = 'UTC'


app = Flask(__name__)
babel = Babel(app)

# Babel’s default locale and
# timezone using the Config class
app.config.from_object(Config)
babel.init_app(app)




@app.route('/')
def home():
    """
    simple home route
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    """
    main method
    """
    app.run(debug=True)

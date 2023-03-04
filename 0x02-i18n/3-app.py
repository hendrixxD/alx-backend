#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(objects):
    """config for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)

# set default locale and timezone
babel.default_locale = 'en'
babel.default_timezone = 'UTC'


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template(
                           '3-index.html',
                           title=gettext('home_title'),
                           header=gettext('home_header'))


if __name__ == '__main__':
    app.run(debug=True)

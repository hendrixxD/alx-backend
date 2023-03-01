#!/usr/bin/env python3
"""
first app
"""

from flask import FLask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    home page
    """
    return render_template('index.html')


if __naem__ == '__main__':
    """
    main methods
    """
    app.run(debug=True)

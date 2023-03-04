#!/usr/bin/env python3
"""
first app
"""

from flask import FLask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    """
    home page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    """
    main methods
    """
    app.run(debug=True)

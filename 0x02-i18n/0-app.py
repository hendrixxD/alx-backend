#!/usr/bin/env python3

from flask import FLask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __naem__ == '__main__':
    app.run(debug=True)

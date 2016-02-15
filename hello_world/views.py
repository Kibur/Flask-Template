__author__ = 'Kibur'

from flask import render_template
from hello_world import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world(username=None):
    return render_template('hellow.html', name=username)

@app.route('/about/')
def about():
    return render_template('about.html')

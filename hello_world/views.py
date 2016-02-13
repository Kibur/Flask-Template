__author__ = 'Kibur'

import logging
from flask import render_template
from hello_world import app

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world(username=None):
    return render_template('hellow.html', name=username)

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_errors(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(Exception)
def all_exceptions_handler(error):
    log.exception('Unhandled exception')
    return render_template('errors/500.html'), 500

__author__ = 'Kibur'

from flask import Flask

# Create Flask Application
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

from . import views, errors

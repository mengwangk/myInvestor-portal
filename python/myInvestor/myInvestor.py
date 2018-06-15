import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)            # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route("/")
def hello():
    return "Hello World!"
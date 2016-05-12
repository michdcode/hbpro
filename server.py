"""One minute getaway."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
import api


app = Flask(__name__)
app.secret_key = 'JMD'

#this will throw an error if a variable is undefined in jinja
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""

    return render_template("home.html")


@app.route('/play')
def getaway():
    """Plays song and shows picture."""

    return render_template("play.html")


@app.route('/location_prob')
def resolve_location():
    """Resolves problem if location not found or no images found."""

    return render_template('location_prob.html')


@app.route('/song_prob')
def resolve_problem():
    """Resolves problem if song has no preview or is explicit"""

    return render_template('song_prob.html')


@app.route('/options')
def provide_options():
    """Provides options once getaway has finished."""

    return render_template('options.html')

if __name__=="__main__":
    app.run(debug=True)

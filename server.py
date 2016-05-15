"""One minute getaway."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
import api

# imported Flash class above, then create an instance of it below
app = Flask(__name__)
app.secret_key = 'JMD'

#this will throw an error if a variable is undefined in jinja
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""

    return render_template("home.html")


@app.route('/songprocess', methods=["POST"])
def song_process():
    """Looks for song and returns song information"""

    song = request.form["sname"]
    api.check_song_data(song)

    if r is 0:
        flash('No songs with that name were found, please enter another song.')
        return redirect('/')
        #the above is temporary really sending to errors
    elif r > 1:
        render_template("song_prob.html", songid_title)
    else:
        songid = songid_title[1]
        api.check_song_data(songid)


@app.route('/song_prob')
def resolve_problem():
    """Resolves problem if song has no preview or is explicit"""

    return render_template('song_prob.html')


@app.route('/select_loc')
def select_location():
    """Select location and validate location."""

    return render_template('select_loc.html')


@app.route('/location_prob')
def resolve_location():
    """Resolves problem if location not found or no images found."""

    return render_template('location_prob.html')


@app.route('/play', methods=["POST"])
def getaway():
    """Plays song and shows picture."""
    return render_template("play.html")


@app.route('/options')
def provide_options():
    """Provides options once getaway has finished."""

    return render_template('options.html')

if __name__ == "__main__":
    app.run(debug=True)
#server only runs if executed from terminal, cannot be imported module

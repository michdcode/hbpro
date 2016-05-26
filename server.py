"""One minute getaway."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from api import obtain_song_URL, get_song_info, get_track_ids, get_song_id_title
from goo_info import obtain_google_api_key
from loginapi import grab_env_variables, requires_auth, callback_handling
import json
import requests

# imported Flash class above, then create an instance of it below
app = Flask(__name__)
app.secret_key = "JMD"
app.jinja_env.undefined = StrictUndefined
#this will throw an error if a variable is undefined in jinja


@app.route('/')
def index():
    """Homepage"""

    return render_template("home.html")


@app.route('/songprocess', methods=["POST"])
def song_process():
    """Looks for song and returns song information"""

    user_song = request.form.get("sname")
    root = get_song_info(user_song)
    track_ids = get_track_ids(root)

    if len(track_ids) == 0:
        return render_template("no_song_found.html")

    elif len(track_ids) > 1:
        songid_title = get_song_id_title(root, track_ids)
        return render_template("song_prob.html", songs=songid_title)

    elif len(track_ids) == 1:
        track_id = track_ids[0].get('id')
        return redirect(url_for("select_location", track_id=track_id))


@app.route('/select_loc', methods=["GET"])
def select_location():
    """Select location and validate location."""

    track_id = request.args.get("track_id")
    google_api = obtain_google_api_key()
    return render_template("select_loc.html", track_id=track_id,
                           google_api=google_api)


@app.route('/play', methods=["GET"])
def getaway():
    """Plays song and shows picture."""

    track_id = request.args.get("track_id")
    track_id = int(track_id)
    surl = obtain_song_URL(track_id)
    lurl = request.args.get("URLphoto")
    locname = request.args.get("locname")
    return render_template("play.html", surl=surl, lurl=lurl, locname=locname)


@app.route('/login')
def social_user_login():
    """Provides login using social media."""

    env_variables = grab_env_variables()
    AUTH0_CLIENT_SECRET = env_variables[0]
    AUTH0_CLIENT_ID = env_variables[1]
    AUTH0_DOMAIN = env_variables[2]
    AUTH0_CALLBACK_URL = env_variables[3]
    return render_template("login.html", AUTH0_CLIENT_SECRET=AUTH0_CLIENT_SECRET,
                           AUTH0_CLIENT_ID=AUTH0_CLIENT_ID, AUTH0_DOMAIN=AUTH0_DOMAIN,
                           AUTH0_CALLBACK_URL=AUTH0_CALLBACK_URL)


@app.route('/callback')
def handle_callback():
    """Callback function for user social login."""
    callback_handling()
    return redirect('/dashboard')


@app.route('/dashboard')
@requires_auth
def dashboard():
    """User information page once logged in."""

    return render_template("dashboard.html", user=session["profile"])


@app.route('/options')
def provide_options():
    """Provides options once getaway has finished."""

    return render_template("options.html")

if __name__ == "__main__":
    app.run(debug=True)
#server only runs if executed from terminal, cannot be imported module

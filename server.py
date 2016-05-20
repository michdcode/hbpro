"""One minute getaway."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, url_for
from api import obtain_song_URL, get_song_info, get_track_ids, get_song_id_title

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
        return redirect(url_for("getaway", track_id=track_id))


@app.route('/select_loc', methods=["GET"])
def select_location():
    """Select location and validate location."""

    return render_template("select_loc.html")


@app.route('/play', methods=["GET"])
def getaway():
    """Plays song and shows picture."""

    track_id = request.args.get("track_id")
    track_id = int(track_id)
    surl = obtain_song_URL(track_id)
    lurl = request.args.get("URLphoto")
    locname = request.args.get("locname")
    return render_template("play.html", surl=surl, lurl=lurl, locname=locname)


@app.route('/options')
def provide_options():
    """Provides options once getaway has finished."""

    return render_template("options.html")

if __name__ == "__main__":
    app.run(debug=True)
#server only runs if executed from terminal, cannot be imported module

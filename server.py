"""One minute getaway."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, url_for
import api
import settings

# imported Flash class above, then create an instance of it below
app = Flask(__name__)
app.secret_key = "JMD"
app.jinja_env.undefined = StrictUndefined
#this will throw an error if a variable is undefined in jinja

settings.init()


@app.route('/')
def index():
    """Homepage"""

    return render_template("home.html")


@app.route('/songprocess', methods=["POST"])
def song_process():
    """Looks for song and returns song information"""

    user_song = request.form["sname"]
    api.check_song_data(user_song)

    # n = cache.get("songnum")
    # s = cache.get("sidntitle")

    if settings.num[0] is 0:
        flash("No songs with that name were found, please enter another song.")
        return redirect('/')
    elif settings.num[0] > 1:
        return redirect('/song_prob')
    elif settings.num[0] is 1:
        gsidtil = settings.songid_title[0][0]
        song = gsidtil[0]
        song = int(song)
        api.obtain_song_URL(song)
        return redirect("settings.sURL[0]", code=302)
        #the call to the URL doesn't work yet
        #redirect(url_for("settings.sURL[0]"))


@app.route('/song_prob')
def resolve_problem():
    """Resolves problem if song has no preview or is explicit"""

    return render_template('song_prob.html', snum=settings.num)


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

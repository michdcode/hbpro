from model import User, Getaway, Song, Location, db


def check_new_user(user_id, user_name):
    """Checks if user is in database and if not adds user to database."""

    if not db.session.query(User).filter(User.user_id == user_id).first():
        newuser = User(user_id=user_id, name=user_name)
        db.session.add(newuser)
        db.session.commit()
        return newuser



def checkin_user(user_id):
    """Grabs user information from database."""

    db_user = db.session.query(User).filter(User.user_id == user_id).first()
    return db_user


def save_current_getaway(user_id, track_id, location_url, location_name, song_name):
    """Saves current getaway information to database."""

    db_user = checkin_user(user_id)
    db_song = get_or_create_song(track_id, song_name)
    db_location = get_or_create_location(location_name, location_url)

    newgetaway = Getaway(user_id=db_user.user_id, track_id=db_song.track_id,
                         location_id=db_location.location_id)

    db.session.add(newgetaway)
    db.session.commit()

    return newgetaway


def get_or_create_song(seven_digital_track_id, song_name):
    """Gets song from database or saves song if not in database."""

    song = db.session.query(Song).filter(Song.seven_digital_track_id == seven_digital_track_id).first()
    if not song:
        song = Song(seven_digital_track_id=seven_digital_track_id, song_name=song_name)
        db.session.add(song)
        db.session.commit()

    return song


def get_or_create_location(loc_name, pict_URL):
    """Gets location from database or saves location if not in database."""

    location = db.session.query(Location).filter(Location.loc_name == loc_name).first()
    if not location:
        location = Location(loc_name=loc_name, pict_URL=pict_URL)
        db.session.add(location)
        db.session.commit()

    return location


def prior_getaways(user_id):

    db_user = checkin_user(user_id)
    getaways = db_user.getaways

    return getaways


def get_getaway(getaway_id):

    getaway = db.session.query(Getaway).filter_by(getaway_id=getaway_id).first()

    return getaway

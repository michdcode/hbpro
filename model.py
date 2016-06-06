from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User of website."""

    __tablename__ = "users"

    user_id = db.Column(db.String(50), nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=db.func.now())


class Getaway(db.Model):
    """Getaway information."""

    __tablename__ = "getaways"

    getaway_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.user_id'))
    track_id = db.Column(db.Integer, db.ForeignKey('songs.track_id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    created = db.Column(db.DateTime, default=db.func.now())

    # Define a relationship to user
    user = db.relationship("User", backref=db.backref("getaways",
                                                      order_by=getaway_id))

    # Define a relationship to songs
    song = db.relationship("Song", backref=db.backref("getaways",
                                                      order_by=getaway_id))

    # Define a realationship to location
    location = db.relationship("Location", backref=db.backref("getaways",
                                                              order_by=getaway_id))


class Song(db.Model):
    """Songs for getaways."""

    __tablename__ = "songs"

    track_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    seven_digital_track_id = db.Column(db.Integer, nullable=False)
    song_name = db.Column(db.String(75), nullable=False)


class Location(db.Model):
    """Locations of getaways."""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    loc_name = db.Column(db.String(100), nullable=False)
    pict_URL = db.Column(db.String(200), nullable=False)


################################################################################
def connect_to_db(app, databaseURI='postgresql:///getawaysdb'):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = databaseURI
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def example_data():
    jane = User(name="jane", user_id="123")
    sf = Location(loc_name="San Francisco", pict_URL="http://www.picture.com/puppy")
    asong = Song(seven_digital_track_id=3326, song_name="happy")
    getaway = Getaway(user=jane, location=sf, song=asong)
    db.session.add_all([jane, sf, asong, getaway])
    db.session.commit()

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."

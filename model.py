from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, request, session

db = SQLAlchemy()


class User(db.Model):
    """User of website."""

    __tablename__ = "users"

    user_id = db.Column(db.String(50), nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        """Provides helpful information on screen."""

        return "<User user_id=%s name=%s created=%s>" % (self.user_id,
                                                         self.name,
                                                         self.created)


class Getaway(db.Model):
    """Getaway information."""

    __tablename__ = "getaways"

    getaway_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.user_id'))
    track_id = db.Column(db.Integer, db.ForeignKey('songs.track_id'))
    loc_name = db.Column(db.String, db.ForeignKey('locations.loc_name'))
    pict_URL = db.Column(db.String(200), nullable=False)
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

    def __repr__(self):
        """Provides helpful information on screen."""

        return "<Getaway getaway_id=%s app_id=%s track_id=%s loc_name=%s>" % (
            self.getaway_id, self.user_id, self.track_id, self.loc_name)


class Song(db.Model):
    """Songs for getaways."""

    __tablename__ = "songs"

    track_id = db.Column(db.Integer, nullable=False, primary_key=True)

    def __repr__(self):
        """Provides helpful information on screen."""

        return "<Song track_id=%s>" % (self.track_id)


class Location(db.Model):
    """Locations of getaways."""

    __tablename__ = "locations"

    loc_name = db.Column(db.String(100), nullable=False, primary_key=True)
    pict_URL = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provides helpful information on screen."""

        return "<Location loc_name=%s>" % (self.loc_name)


################################################################################
def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///getawaysdb'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."

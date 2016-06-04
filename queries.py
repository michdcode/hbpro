from flask import Flask, request, session, url_for, jsonify
from model import User, Getaway, Song, Location, db
import json


def check_new_user(user):
    """Checks if user is in database and if not adds user to database."""

    auser_find = user['user_id'].split("|")
    auser_id = auser_find[1]
    aname = user['name']
    #only Twitter has location information

    if not db.session.query(User).filter(User.user_id == auser_id).first():
        newuser = User(user_id=auser_id, name=aname)
        db.session.add(newuser)
        db.session.commit()


def checkin_user(user):
    """Grabs user information from database."""

    user_find = user['user_id'].split("|")
    user_id = user_find[1]
    db_user = db.session.query(User).filter(User.user_id == user_id).first()
    return db_user


def save_current_getaway(user):
    """Saves current getaway information to database."""
    db_user = checkin_user(user)

    atrack_id = session.get("track_id")
    alurl = session.get("lurl")
    alocname = session.get("locname")
    asongname = session.get("song_name")
    db_song = get_or_create_song(atrack_id, asongname)
    db_location = get_or_create_location(alocname, alurl)

    newgetaway = Getaway(user_id=db_user.user_id, track_id=db_song.track_id,
                         location_id=db_location.location_id)

    db.session.add(newgetaway)
    db.session.commit()

    return newgetaway


def get_or_create_song(seven_digital_track_id, song_name):
    """Gets song from database or saves location if not in database."""

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


def prior_getaways(user):

    db_user = checkin_user(user)
    getaways = db_user.getaways

    return getaways


def get_getaway(getaway_id):

    getaway = db.session.query(Getaway).filter_by(getaway_id=getaway_id).first()

    return getaway

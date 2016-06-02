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
    db_song = get_or_create_song(atrack_id)

    newgetaway = Getaway(user_id=db_user.user_id, track_id=db_song.track_id)

    db.session.add(newgetaway)
    db.session.commit()

    return newgetaway


def get_or_create_song(seven_digital_track_id):

    song = db.session.query(Song).filter(Song.seven_digital_track_id == seven_digital_track_id).first()
    if not song:
        song = Song(seven_digital_track_id=seven_digital_track_id)
        db.session.add(song)
        db.session.commit()

    return song


def prior_getaways(user):

    db_user = checkin_user(user)
    getaways = db_user.getaways
    return getaways

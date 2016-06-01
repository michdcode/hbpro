from flask import Flask, request, session, url_for, jsonify
from model import *
from image_finder import get_option_images
import json


def user_look_up(user):
    """Checks if user is in database and if not adds user to database."""

    auser_find = user['user_id'].split("|")
    auser_id = auser_find[1]
    aname = user['name']
    #only Twitter has location information

    track_id = session.get("track_id")
    lurl = session.get("lurl")
    locname = session.get("locname")
    print track_id, lurl, locname

    if not db.session.query(User).filter(User.user_id == auser_id).first():
        newuser = User(user_id=auser_id, name=aname)
        db.session.add(newuser)
        db.session.commit()


# def checkin_user(user):
#     """Checks in user and grabs user information from database."""

#     user_find = user['user_id'].split("|")
#     user_id = user_find[1]
#     db_user = User.query.filter(User.user_id).first()
#     print user_id, db_user


def save_current_getaway():
    """Saves current getaway information to database."""

    atrack_id = session.get("track_id")
    alurl = session.get("lurl")
    alocname = session.get("locname")



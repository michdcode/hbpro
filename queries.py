from flask import Flask, request, session, url_for, jsonify
from model import *
from image_finder import get_option_images
import json


def user_look_up(user):
    """Checks if user is in database and if not adds user"""

    print
    auser_find = user['user_id'].split("|")
    auser_id = auser_find[1]
    aname = user['name']
    #only Twitter has location information
    if user['location']:
        auser_location = user['location']
    else:
        auser_location = None

    if not db.session.query(User).filter(User.user_id == auser_id).first():
        user = Users(user_id=auser_id, name=aname, user_location=auser_location)
        db.sesssion.add(user)
        db.sesssion.commit()


def checkin_user(user):
    """Checks in user and grabs user information from database."""

    user_find = user['user_id'].split("|")
    user_id = user_find[1]
    db_user = User.query.filter(User.user_id).first()
    print user_id, db_user

import os
import json
import requests
from functools import wraps
from flask import session, jsonify, request


def grab_env_variables():
    """Gets variables from environ and stores in list."""
    env_variables = []
    env_variables.append(os.environ['AUTH0_CLIENT_SECRET'])
    env_variables.append(os.environ['AUTH0_CLIENT_ID'])
    env_variables.append(os.environ['AUTH0_DOMAIN'])
    env_variables.append(os.environ['AUTH0_CALLBACK_URL'])
    return env_variables


# Requires authentication annotation
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated


def callback_handling():
    """Handles callback operation."""
    code = request.args.get('code')
    json_header = {'content-type': 'application/json'}
    token_url = "https://{domain}/oauth/token".format(domain=os.environ['AUTH0_DOMAIN'])
    token_payload = {
        'client_id': os.environ['AUTH0_CLIENT_ID'],
        'client_secret': os.environ['AUTH0_CLIENT_SECRET'],
        'redirect_uri': os.environ['AUTH0_CALLBACK_URL'],
        'code': code,
        'grant_type': 'authorization_code'}

    token_info = requests.post(token_url, data=json.dumps(token_payload), headers=json_header).json()

    user_url = "https://{domain}/userinfo?access_token={access_token}".format(
        domain=os.environ['AUTH0_DOMAIN'], access_token=token_info['access_token'])

    user_info = requests.get(user_url).json()

    session['profile'] = user_info

# requires_auth & callback_handling functions are largely taken from Auto0 official documentation.

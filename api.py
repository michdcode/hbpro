import oauth2 as oauth
import os
import requests
import xml.etree.ElementTree as ET


def obtain_song_URL(track_id):
    """Obtains oauth signature and URL to play song preview."""

    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    request_url = "http://previews.7digital.com/clip/%d?country=US" % (track_id)

    req = oauth.Request(method="GET", url=request_url, is_form_encoded=True)

    req['oauth_timestamp'] = oauth.Request.make_timestamp()
    req['oauth_nonce'] = oauth.Request.make_nonce()
    sig_method = oauth.SignatureMethod_HMAC_SHA1()

    req.sign_request(sig_method, consumer, token=None)
    sURL = req.to_url()
    return sURL
    #function above is largely taken from user filip at this location:
    #https://groups.google.com/forum/#!msg/7digital-api/cM8zuQoThiw/tTVRsMCvs7UJ


def get_song_info(user_song):
    """7digital API call for song info, turn XML result into ElementTree."""

    consumer_key = os.environ['consumer_key']
    payload = {'q': user_song, 'oauth_consumer_key': consumer_key,
               'country': 'US', 'usageTypes': 'download'}

    url = 'http://api.7digital.com/1.2/track/search?'

    result = requests.get(url, payload)
    asc2 = result.text.encode('ascii', 'ignore')
    root = ET.XML(asc2)
    return root


def get_track_ids(root):
    """Iterate over sub-tree to obtain track_ids."""

    track_ids = []
    for track in root.iter('track'):
        track_ids.append(track.attrib)
    return track_ids


def get_song_id_title(root, track_ids):
    """Iterate over sub-tree to obtain song name and match to track id."""

    titles = []
    for title in root.iter('title'):
        titles.append(title.text)
    del titles[::-2]
    track_ids = [li['id'] for li in track_ids]
    songid_title = zip(track_ids, titles)
    return songid_title

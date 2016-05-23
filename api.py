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
    # request_url = "http://previews.7digital.com/clip/9909481?country=US"
    # must replace the numbers in URL with trackid for selected song

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
    """Make API call for info about song & put in usable format."""

    consumer_key = os.environ['consumer_key']
    payload = {'q': user_song, 'oauth_consumer_key': consumer_key,
               'country': 'US', 'usageTypes': 'download'}

    url = 'http://api.7digital.com/1.2/track/search?'

    result = requests.get(url, payload)
    # """test one: is the URL encoded properly
    # result one: yes: http://api.7digital.com/1.2/track/search?
    # q=happy&country=US&oauth_consumer_key=[omitted]&usageTypes=download
    # """
    root = ET.XML(result.text)
    return root
    # returns an object <Element 'response' at 0x10ae65e10>


def get_track_ids(root):
    """Parse root and grab track id."""
    track_ids = []
    for track in root.iter('track'):
        track_ids.append(track.attrib)
    return track_ids
    # grabs the track id of all songs and turns it into a list of
    # dictionaries {'id': '33576075'}


def get_song_id_title(root, track_ids):
    titles = []
    for title in root.iter('title'):
        titles.append(title.text)
    # grabs the title of the song and the title of the album
    del titles[::-2]
    # deletes the album title from titles list
    track_ids = [li['id'] for li in track_ids]
    # deletes keys ('id') in track id list, so list only has track ids
    songid_title = zip(track_ids, titles)
    # the above matches the track ids and titles into one list
    # sample tests confirm that the matching is correct in terms of id & song
    return songid_title

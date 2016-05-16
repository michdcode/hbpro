import oauth2 as oauth
import os
import requests
import xml.etree.ElementTree as ET
import settings


#changing this from an individual script to a function
def obtain_song_URL(song):
    """Obtains oauth signature and URL to play song preview."""

    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    #must replace the numbers in URL with trackid for selected song
    request_url = "http://previews.7digital.com/clip/%d?country=US" % (song)

    req = oauth.Request(method="GET", url=request_url, is_form_encoded=True)

    req['oauth_timestamp'] = oauth.Request.make_timestamp()
    req['oauth_nonce'] = oauth.Request.make_nonce()
    sig_method = oauth.SignatureMethod_HMAC_SHA1()

    req.sign_request(sig_method, consumer, token=None)

    settings.sURL.append(req.to_url())

    #right now this prints to terminal, but will need to send URL for other use
    # print req.to_url()


def check_song_data(song):
    """Find out if song is in database, if so return song_id"""

    consumer_key = os.environ['consumer_key']
    payload = {'q': song, 'oauth_consumer_key': consumer_key, 'country': 'US',
               'usageTypes': 'download'}

    url = 'http://api.7digital.com/1.2/track/search?'

    result = requests.get(url, payload)
    # """test one: is the URL encoded properly
    # result one: yes: http://api.7digital.com/1.2/track/search?
    # q=happy&country=US&oauth_consumer_key=[omitted]&usageTypes=download
    # """

    root = ET.XML(result.text)
    count_song_results(root)
    # print root - test to see if get object back
    # yes, the above returns an object <Element 'response' at 0x10ae65e10>


def count_song_results(root):
    """Count results and determine next step"""
    # #the above evaluates the number of results
    track_ids = []
    for track in root.iter('track'):
        track_ids.append(track.attrib)

    print track_ids
    settings.num.append(len(track_ids))
    print settings.num
    # the above grabs the track id of all songs and turns them into a list of
    # dictionaries {'id': '33576075'}
    titles = []
    for title in root.iter('title'):
        titles.append(title.text)
    # the above grabs the title of the song and the title of the album
    del titles[::-2]
    print titles
    # the above deletes the album title
    track_ids = [li['id'] for li in track_ids]
    # the above deletes keys, which are all 'id', now the list has the track ids
    settings.songid_title.append(zip(track_ids, titles))
    # the above matches the track ids and titles into one list
    # sample tests confirm that the matching is correct in terms of id & song
    # print songid_title

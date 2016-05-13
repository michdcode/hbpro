import oauth2 as oauth
import os
import requests
import xml.etree.ElementTree as ET


#changing this from an individual script to a function
def obtain_song_URL():
    """Obtains oauth signature and URL to play song preview."""

    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    #must replace the numbers in URL with trackid for selected song
    request_url = "http://previews.7digital.com/clip/569975?country=US"

    req = oauth.Request(method="GET", url=request_url, is_form_encoded=True)

    req['oauth_timestamp'] = oauth.Request.make_timestamp()
    req['oauth_nonce'] = oauth.Request.make_nonce()
    sig_method = oauth.SignatureMethod_HMAC_SHA1()

    req.sign_request(sig_method, consumer, token=None)

    #right now this prints to terminal, but will need to send URL for other use
    print req.to_url()


def check_song_data(song):
    """Find out if song is in database, if so return song_id"""

    consumer_key = os.environ['consumer_key']
    payload = {'q': song, 'oauth_consumer_key': consumer_key, 'country': 'US',
               'usageTypes': 'download'}

    url = 'http://api.7digital.com/1.2/track/search?'

    # print (r.url)
    # """test one: is the URL encoded properly
    # result one: yes: http://api.7digital.com/1.2/track/search?
    # q=happy&country=US&oauth_consumer_key=[omitted]&usageTypes=download
    # """

    result = requests.get(url, payload)
    root = ET.XML(result.text)
    print root
    # return root
    # the above returns an object <Element 'response' at 0x10ae65e10>

    for item in root.findall('searchResults'):
        num = item.find('totalItems').text
        print num
    # the above returns the number of results from the search
        if int(num) is 0:
            print "none"
        elif int(num) is 1:
            print "one"
        else:
            pass
    #the above evaluates the number of results
    for track in root.iter('track'):
        print track.attrib
    #the above grabs the track id of all songs in this dict format with a return
    # between each one {'id': '33576075'}
    for title in root.iter('title'):
        print title.text
    #this is the titles problem is that two titles, both of which are children
    #exist, the first one is the song title, the second is the album title.



# def process_song_data(result):
#     """Turn XML data into string and determine next step"""

#     root = ET.fromstring(result)

#     print type(root)

    # for item in root.findall('searchResults'):
    #     num = item.find('pageSize').text
    #     print num
    # right now print to the terminal & look at encoding

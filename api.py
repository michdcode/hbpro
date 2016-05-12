import oauth2 as oauth
import os


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


#call function only for test purposes
# obtain_song_URL()


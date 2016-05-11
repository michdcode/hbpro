import oauth2 as oauth
import os

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
consumer = oauth.Consumer(consumer_key, consumer_secret)
request_url = "http://previews.7digital.com/clip/132028?country=US"

req = oauth.Request(method="GET", url=request_url, is_form_encoded=True)

req['oauth_timestamp'] = oauth.Request.make_timestamp()
req['oauth_nonce'] = oauth.Request.make_nonce()
sig_method = oauth.SignatureMethod_HMAC_SHA1()

req.sign_request(sig_method, consumer, token=None)

print req.to_url()

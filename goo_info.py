import os


def obtain_google_api_key():
    """Gets goole api key from session"""

    google_api = os.environ['google_api']
    return google_api

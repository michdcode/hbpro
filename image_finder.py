

def get_option_images():
    """Gets icons and URL's for options page."""

    images = [
        {"id": 1,
         "source": "static/img/shopping-cart.png",
         "url": "https://us.7digital.com/",
         "label": "BUY SONG"},
        {"id": 2,
         "source": "static/img/musical-note.png",
         "url": "/play",
         "label": "REPLAY GETAWAY"},
        {"id": 3,
         "source": "static/img/play-button.png",
         "url": "/login",
         "label": "SAVE GETAWAY (login)"},
        {"id": 4,
         "source": "static/img/planet-earth.png",
         "url": "https://www.expedia.com/",
         "label": "BOOK TRAVEL"},
        {"id": 5,
         "source": "static/img/home.png",
         "url": "/",
         "label": "NEW GETAWAY"},
        {"id": 6,
         "source": "static/img/playlist.png",
         "url": "/login",
         "label": "REPLAY PRIOR GETAWAYS (login)"}
    ]
    return images

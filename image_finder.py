

def get_option_images():
    """Gets images and URL's for various options."""
    images = [
        {"id": 1,
         "source": "static/img/music-player.png",
         "url": "https://us.7digital.com/",
         "label": "buy song"},
        {"id": 2,
         "source": "static/img/music-player-replay.png",
         "url": "/play",
         "label": "replay getaway"},
        {"id": 3,
         "source": "static/img/save.png",
         "url": "/login",
         "label": "save getaway (login)"},
        {"id": 4,
         "source": "static/img/black-plane.png",
         "url": "https://www.expedia.com/",
         "label": "book travel"},
        {"id": 5,
         "source": "static/img/home-button.png",
         "url": "/",
         "label": "new getaway"},
        {"id": 6,
         "source": "static/img/share.png",
         "url": "/login",
         "label": "share getaway (login)"}
    ]
    return images

class Movie():
    """A moive class which stores the movie information.
    
    Attributes:
        title: a string of the the movie title.
        poster_image_url: a string of the url linking to a poster of this movie.
        trailer_youtube_url: a string of the YOUTUBE url that contains the movie trailer of the movie.
    """
    
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits Movie with necessary variables."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
class Movie():
    """Represents a Movie and their properties."""
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Creates a new instance of movie with the arguments passed
        as parameters."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

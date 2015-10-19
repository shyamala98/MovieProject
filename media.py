""" This module defines the Movie class """


class Movie(object):
    """ The Movie class encapsulates information for a movie

    Attributes:
        title(str): Human readable string specifying the title for the movie
        story(str): Human readable string describing the story line for the movie
        trailer_youtube_url: string specifying the url for the youtube movie trailer
        poster_image_url: string specifying the url for the movie poster

    """

    def __init__(self, title, story, trailer_youtube_url=None, poster_image_url=None):
        self.title = title
        self.story_line = story
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url


def main():
    pass

# test
if __name__ == '__main__':
    main()

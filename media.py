#-------------------------------------------------------------------------------
# Name:        Movie Trailer
# Purpose:
#
# Author:      shyamala
#
# Created:     28/09/2015
#-------------------------------------------------------------------------------
import webbrowser

class Movie():
    def __init__(self, title, story, trailer_youtube_url=None, poster_image_url=None):
        self.title = title
        self.story_line = story
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url


def main():
    pass
#test
if __name__ == '__main__':
    main()

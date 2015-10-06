#-------------------------------------------------------------------------------
# Name:        Movie Trailer
# Purpose:
#
# Author:      shyamala
#
# Created:     28/09/2015
#-------------------------------------------------------------------------------
import webbrowser

class Movie(object):
    def __init__(self, title, story, trailorUrl=None, posterUrl=None):
        self.title = title
        self.story = story
        self.trailorUrl = trailorUrl
        self.posterUrl = posterUrl

    def play_trailor(self):
        pass

def main():
    pass

if __name__ == '__main__':
    main()

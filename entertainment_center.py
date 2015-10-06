#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      shyamala
#
# Created:     05/10/2015
# Copyright:   (c) shyamala 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import media
import fresh_tomatoes

def main():
    #Create a list of movies
    list_of_movies = []
    #Fill in the movie details
    movie = media.Movie("Toy Story", "A Story of a boy and his toys that come to life", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" )
    list_of_movies.append(movie)

    fresh_tomatoes.open_movies_page(list_of_movies)


if __name__ == '__main__':
    main()

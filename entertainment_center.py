#-------------------------------------------------------------------------------
# Name:        entertainment_center
# Author:      shyamala Prakash
#
#-------------------------------------------------------------------------------
import media
import fresh_tomatoes

# Creates and returns a list of movies, for the time being the movie titles and other details are hard coded
def getMovieList():
    #Create a list of movies
    list_of_movies = []
    #Fill in the movie details
    movie = media.Movie("Sicario", "Set in the US-Mexican order, a story about the war on drugs", "https://www.youtube.com/watch?v=G8tlEcnrGnU", "http://t3.gstatic.com/images?q=tbn:ANd9GcT4oUDoLOJuqZNW-rZGnc4TquZoOKcNmkwCgDzikSL6enj4XH7R" )
    list_of_movies.append(movie)
    movie = media.Movie("Dior and I", "A beautifully tailored documentary for fashion fans", "https://www.youtube.com/watch?v=Sd_qAzoCpiI", "http://t3.gstatic.com/images?q=tbn:ANd9GcSyW8DYQ8U6HCd9bakNlB13BGJm5-hBd5uLXRxFaKMfL-5eaPRi" )
    list_of_movies.append(movie)
    movie = media.Movie("CITIZENFOUR", "Edward Snowden Documentary", "https://www.youtube.com/watch?v=oKkF-X4QLB4", "https://i.ytimg.com/vi_webp/oKkF-X4QLB4/movieposter.webp")
    list_of_movies.append(movie)
    movie = media.Movie("IRIS", "IRIS pairs the late Albert Maysles filmmaker with Iris Apfel, the quick-witted, flamboyantly dressed 93-year-old style maven who has had an outsized presence on the New York fashion scene", "https://www.youtube.com/watch?v=Fo8jwJ_2l0c", "http://ia.media-imdb.com/images/M/MV5BNDMzMDY1NTE4MV5BMl5BanBnXkFtZTgwODc4NjY3NDE@._V1_SX214_AL_.jpg")
    list_of_movies.append(movie)
    movie = media.Movie("I'll See You In My Dreams", "A widow and former songstress discover that life can begin anew at any age", "https://www.youtube.com/watch?v=5AhP-EeIMc4", "http://resizing.flixster.com/Y0YOf1p_b_GSol1_FmdAL6RRJy8=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/10/11191061_ori.jpg")
    list_of_movies.append(movie)
    movie = media.Movie("Meet the Patels", "Filmmaker Geeta V. Patel follows her brother, Indian-American actor Ravi V. Patel, as he embarks on a quest to find a wife and make his family happy.", "https://www.youtube.com/watch?v=7litSYXbpRs", "http://t0.gstatic.com/images?q=tbn:ANd9GcQKtzHY5sdi6pT57onT6_78zfbNwJGuM23-pMVKBbAyOSr9SVTQ")
    list_of_movies.append(movie)

    return list_of_movies


def main():
    #Get the list of movies
    list_of_movies = getMovieList()
    #Create the html page fresh_tomatoes.html, launch the default webbrowser and load fresh_tomatoes.html
    fresh_tomatoes.open_movies_page(list_of_movies)

if __name__ == '__main__':
    main()

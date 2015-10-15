Project: Movie Trailer Website  - [Shyamala Prakash]
================================
Creates a web page with 6 movie titles. Opens the page using the default web browser. Clicking on the poster image for a movie, launches the trailer for the movie.
Url for the project on Git: https://github.com/shyamala98/MovieProject.git

Required Libraries and Dependencies
-----------------------------------
Requires Python v2.* (Download site)

Make sure the directory containing python.exe is in your PATH variable

How to Run Project
------------------
Clone the MovieTrailer project from Git to your local machine

Running the project from Windows command line:<br/>
python \<Local Directory where project is cloned\>/MovieProject/entertainment_center.py

Running the project from the python shell:<br/>
Launch the python shell. <br/>
You will have to change the current directory to be the directory where the module entertainment_center.py lives, for example, the directory where you cloned 
this repository locally is C:\cloneRepos, execute the following commands in the python shell

\>\>\>import os <br/>
\>\>\>os.chdir('C:\cloneRepos\MovieProject') <br/>
\>\>\>execfile('entertainment_center.py')


Extra Credit Description
------------------------
A flyout (popover) with the movie storyline is displayed when the user hovers on the image for the movie.
The style attributes for the popover were copied from sample code in w3schools website - http://www.w3schools.com/bootstrap/bootstrap_ref_js_popover.asp
The Bootstrap popover plugin feature was used to implement this feature. Changes were made in the file fresh_tomatoes.py


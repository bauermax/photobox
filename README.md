

![N|Solid](http://maximebauer.com/easyupload/assets/files/09f1ec20-photoedited.jpg)
# PHOTOBOX
This photobox was a project created from scratch; from the 3D models to the photobox software.
In this repository, you will find :

  - The python program for the photobox
  - The php server sources to host your photos
  - The 3D model for the photobox (coming soon...)

# Python side

  - Working with python 2.7 & 3.x
  - Libraries: PIL, time, yaml, requests, hashlib, RPI.GPIO, picamera
  - Configuration via 'config.yaml' (server security, server url, placeholder image etc...)

# PHP server side

  - Working with apache or nginx
  - Configuration via config.ini
  - Can easily be replaced by a custom server application (the python app is sending POST requests)

# Overall functioning
This repository contains 2 projects, a python client and a PHP server.
When you run the python project, you will see a camera preview, and you can press the left or right button to change a filter, or press the big button on the middle to capture a photo. Once captured, the photo will be processed to add a logo (if the option is enabled in the config file) and then uploaded to the server. If there is no internet connexion, the photo will be stored in a temp folder and uploaded at the next launch of the program (if an internet connexion is available).
You can edit many parameters is the config file (if you want to add a logo or not, the server url, the server token, the different folders, the GPIO ports, the camera resolution...).

The PHP program is splitted in 2 parts : The part which handle uploads, and the other part which displays the photos. There is also an admin interface (that you can restrict with .htpasswd) where you can delete photos.

Contact
----
If you want to ask a question about he project, or if you have any issue, you can contact me  :
 - Facebook : https://www.facebook.com/Bauer.Maxime
 - Email : maxime.bauer.mb@gmail.com
 - Or via github

License
----
**Open source software, feel free to use it !**

Software developed by Maxime Bauer (maxime.bauer.mb@gmail.com) with the help of Maxime Ball (maxime.ball@viacesi.fr)
3D conception by Mickaël Marty (mickael.marty@viacesi.fr)

This project was funded by the Exia.Cesi engineering school (Strasbourg)

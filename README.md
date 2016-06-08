*One Minute Getaway*
===========
Learn more about the developer: www.linkedin.com/in/michelletdicks

One Minute Getaway is a fullstack web application intended to allow users to take a one minute vacation. A user can enter a song of their choice, and with the integration of the 7digital API, the correct version of the song is determined, and a preview of the song it obtained. Next, the user can select any location across the globe. With the integration of the google maps API, using the autocomplete feature, the user does not have to worry about spelling errors, and it will even suggest locations as the user types. Once the location is selected, the Places Library within the Google Maps API will obtain a picture of that location. The preview of the song will play, while a picture of the location is displayed, allowing the user to have a brief one minute getaway. 

The user then has the option to purchase the song from 7 digital, as the music is the central point of the experience Alternately, a user can replay the getaway, or go to Expedia and purchase travel. A user can also login using a SSO through the use of the Auth0 API, which is configured to allow Facebook, Twitter and Google based logins, or the user can create a seperate login for the app. Once logged in, the user can save the getaway, set a list of prior getaways and replay a prior getaway.

![Homepage](https://github.com/michdcode/hbpro/blob/master/for_readME/homepage.png)
![Location](https://github.com/michdcode/hbpro/blob/master/for_readME/location.png)

#### Technologies
Python, Flask, PostGres, SQLAlchemy, HTML, CSS, Bootstrap, Javascript, 7digital API, Google Maps API (Places Library), Auth0 API

(Dependences are contained in requirements.txt)

#### Testing
Currently, 82% of the app has been tested, including 100% of the actions involving the database.  
![Testing](https://github.com/michdcode/hbpro/blob/master/for_readME/test_results.png)

#### API Usage
The seven digital library contains data for over 30 million songs, and was previously used to power song purchases for the Spotify app. The primary reason for the selection of the 7digital API is that it is well documented and contains previews for the majority of songs available. The first API call is to search for the song, and the second API call is to obtain a song preview URL. All calls to the seven digital API are done from the backend, in Python, for speed. Only the track id and song name are stored in the database, no other song information is stored. 

The Google Maps API was selected because the autocomplete feature provides active assistance to users, which enhances the UI/UX experience. The final name of the location is the Google Maps name for the location, which leads to better data quality in the Postgres database if a user chooses to save a Getaway. Lastly, the Places Library contains up to ten pictures for each location, which guarantees a result in most instances and prevents having to use another API to obtain a picture. The first API call allows for the use of the autocomplete feature and selection of the location name, and the second API call is to obtain the URL for the picture of the location. All calls to the Google Maps API are done from the frontend, in JavaScript, for user interactivity. 

The Auth0 API was selected because it manages the entire login function and is customizeable. Users expect to use social media credentials to login to an application. Auth0 allows developers to choose which social media providers to integrate with, and will obtain user information once a user logs in that can then be stored in the PostGres database. It can also be configured to allow for a login to the web app itself. Auth0 sends an automatic welcome email that can be customized, provides a lost password function, and updates for any changes that social media platforms make to their login API's. It also manages security, which is always a consideration for a login function. Multiple calls are made to the Auth0 API. 

### Structure of main components

#####api.py
Backend components for using the 7digital API.

#####loginapi.py
Frontend components for using the Google maps API. 

#####model.py
SQLAlchemy Integration with Postgres, object oriented database model.

#####queries.py
All queries, storage and other interactions with the Postgres database. 

#####server.py
The core of the app, showing all Flask routes.

#####static
The folder contains three subfolders: (1) img: images used by the app, but not location images from Google; (2) css: external css files for various pages for the app; (3) js: javascript file for certain functionality for the app. 

#####templates
The folder contains all web pages used for the app.

#####unittest_queries
Contains the tests performed on the app. 

### Future Upgrades

###### Getaway recommendations 
I want to look at the songs and locations that users have selected and predict getaways that the user might like.

###### Social sharing 
Users may enjoy sharing their getaways with others using social media.

###### UI/UX enhancement 
The app can be modified to provide a better user experience visually and in terms of user flow.
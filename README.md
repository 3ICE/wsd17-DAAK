# TIE-23500, Web Programming, Spring 2017
Teachers: Petri Ihantola, Mikko Nurminen

# Web Software Development - Daniel, Aparajita, Arjun, Krishna
## Group ID: `wsd17-DAAK`
This repo created 2017. 02. 23. by Arjun.

Readme written on 2017. 02. 25. by Daniel.

Project description [Google doc](https://docs.google.com/document/d/1-ewnhsmQUpAdAhg6CiAEs34RXeRC5-dZ1wzEM0eZJ-A/edit)

My Web development repo: https://gitlab.rd.tut.fi/berezvai/web/

Master `seitti2017` repo: https://gitlab.rd.tut.fi/seitti/seitti2017/tree/master

## Members:
* Daniel Berezvai, <daniel.berezvai@student.tut.fi>
* Aparajita Chowdhury, <aparajita.chowdhury@student.tut.fi>
* Arjun Venkatakrishnan, <arjun.venkatakrishnan@student.tut.fi>
* Krishna Bagale, <krishna.bagale@student.tut.fi>


## Useful command line instructions:
Git global setup (do this once)
```
git config --global user.name "Firstname Lastname"
git config --global user.email "first.last@student.tut.fi"
```

Download this repository (only once)
```
git clone git@gitlab.rd.tut.fi:venkatak/wsd17-DAAK.git
```

Make sure you are in the correct folder (every time)
```
cd wsd17-DAAK
```

Update your local files with all our latest commits (before you make changes)
```
git pull
```

Add all files you modified (after you're finished with a task)
```
git status
git add .
git commit -m "hi"
git push
```

Have fun, web developers!

Daniel


Our first task is this:
```
General description of what you are doing and how you are doing that (what kinds of views, models are needed),
how they relate to each other, and what is the implementation order and timetable.

In the project plan your group will at least tell the following:
students in your group (names, email addresses, student ids)
name of your group
what of the listed features we plan to implement:
Register as a player and developer
As a developer: add games to their inventory, see list of game sales
As a player: buy games, play games, see game high scores and record their score to it
Authentication:
Login, logout and register (both as player or developer).  See documentation about extending the User model https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#extending-the-existing-user-model
Email validation is required. For dealing with email in Django see https://docs.djangoproject.com/en/1.8/topics/email/#email-backends You do not need to configure a real SMTP-server, using Django's Console Backend is enough.
Use Django auth
Basic player functionalities:
Buy games, payment is handled by a mockup payment service: 
Play games. See also game/service interaction
Security restrictions, e.g. player is only allowed to play the games they’ve purchased
Also consider how your players will find games (are they in a category, is there a search functionality?)
Basic developer functionalities:
Add a game (URL) and set price for that game and manage that game (remove, modify)
Basic game inventory and sales statistics (how many of the developers' games have been bought and when)
Security restrictions, e.g. developers are only allowed to modify/add/etc. their own games, developer can only add games to their own inventory, etc.


Game/service interaction:
When player has finished playing a game (or presses submit score), the game sends a postMessage to the parent window containing the current score. This score must be recorded to the player's scores and to the global high score list for that game. See section on Game Developer Information for details.
Messages from service to the game must be implemented as well
Quality of Work will be high
Quality of code (structure of the application, comments)
Purposeful use of framework (Don't-Repeat-Yourself principle, Model-View-Template separation of concerns)
User experience (styling, interaction)
Meaningful testing
Non-functional requirements:
This Project plan
Overall documentation, demo, teamwork, and project management as seen from the history of your GitLab project (and possible other sources that you submit in your final report)
Own JavaScript game
Develop a (simple) game in JavaScript that communicates with the service (the game has to use at least these three service features: high score, save, load)
The will be deployed somewhere. Note that games may be possible to deploy as static content as many of them do not require backend - other than the game store (If you'd like to deploy games to heroku as well, it can be in it’s own project in GitLab. If this is the case, please share this project to wsd-agent and link the project from your main repository)
Extra functionality:
Save/load and resolution feature
The service supports saving and loading for games with the simple message protocol described in Game Developer Information
3rd party login
Allow OpenID, Gmail or Facebook login to your system. This is the only feature where you are supposed to use third party Django apps in your service.
RESTful API
Design and Implement some RESTful API to the service
E.g. showing available games, high scores, showing sales for game developers (remember authentication)
Mobile Friendly
Attention is paid to usability on both traditional computers and mobile devices (smart phones/tablets)
It works with devices with varying screen width and is usable with touch based devices (see e.g. http://en.wikipedia.org/wiki/Responsive_web_design )
Social media sharing
Enable sharing games in some social media site (Facebook, Twitter, Google+, etc.)
Focus on the metadata, so that the shared game is “advertised” well (e.g. instead of just containing a link to the service, the shared items should have a sensible description and an image)
Testing your service with other groups’ games
Use the games other groups’ games, choosing the games from a list when the list becomes available
Give feedback for the game and it’s functioning with your online game store. Make sure your feedback is constructive and professional in tone and in substance.
Feedback will be given using the games list using a mechanism on it, when the list  becomes available later.
High quality of feedback and more than 2 tested programs.
are there some extra features not listed in the project description what you plan to implement?
for each feature, how you are going to implement it
information on how you plan on working on the project  (will you meet face-to-face regularly, will use some project management tools, etc.)

Keep your project plan updated during the project!

````
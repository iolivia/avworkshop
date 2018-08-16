
## Workshop:00 - Intro (5 mins)
Form groups of 3 
Find a team name 
Introduce yourselves to your teammates
Name
What you do
Random fact about yourself
Vim or emacs
Dogs or cats
Worst/favorite programming language


## Workshop:01 - Setup (10 mins)
Pre-requisites
An editor of your choice (Visual Studio Code, Sublime, etc.)
Python3 and pip3
Git 
Chrome or Firefox


Grab the code
git clone https://olivif@bitbucket.org/olivif/avworkshop.git

Run these to install all the python packages needed
pip3 install -r requirements.txt
python3 manage.py runserver

You should see something like this (Ignore any warnings about database migrations)
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Note: You can use a python virtual environment if you don’t want to pollute your global setup. But you don’t have to.

## Workshop:02 – Download video (10 mins)
Manifest URL - http://www.bok.net/dash/tears_of_steel/cleartext/stream.mpd

Download video (add the code in player.html script tag)
BaseURL + representationId + segmentId 

Notes
Pick one representation for now 
Segment ids are sequential, for this piece of content we have 245 segments, but download as many as you want (more than 1 )
Make sure you get ArrayBuffer responses ( you can do this by printing the response of the http request and see an ArrayBuffer type)
Open the developer tools network tab and observe


## Workshop:03 - Open a MediaSource (10 mins)
Create a MediaSource instance 
Link the media source instance to the video element on the page
Hook onto the MediaSource open event 
Make sure the MediaSource opens (add a console.log in the event handler)

https://developer.mozilla.org/en-US/docs/Web/API/MediaSource


## Workshop:04.1 - Play video (10 mins)
Feeding the init fragment 
Add a video source buffer 
Append the init fragment 

Notes:
If you’ve done everything correctly, you should see the duration of the video update (since now we have metadata)

https://developer.mozilla.org/en-US/docs/Web/API/SourceBuffer

## Workshop:04.2 - Play video (10 mins)
Appending video fragments
Add an event listener for updateend event
Append the video we downloaded previously in the updateend handler
Call play programmatically, or press play once on the page


## Workshop:05 - Play audio (15 mins)
Pretty much the same as we did for video


## Workshop:06 – Design adaptive quality levels (15 mins)
Now we’re playing a fixed quality level, but what if our bandwidth is lower than the quality we picked? What if our bandwidth fluctuates while we are watching the video? 
Design an adaptive quality level detection
Start with the lowest quality
Get some measure of how fast we are downloading and increase/decrease the quality level based on that
No need to write code for this one, but think about how you would do it and what information you need to keep track of.

## Workshop:00 - Intro (5 mins)
1. Form groups of 3 
2. Find a team name 
3. Introduce yourselves to your teammates
	1. Name
	2. What you do
	3. Random fact about yourself
	4. Vim or emacs
	5. Dogs or cats
	6. Worst/favorite programming language


## Workshop:01 - Setup (10 mins)

Pre-requisites: 

* An editor of your choice (Visual Studio Code, Sublime, etc.)
* [Python3](https://docs.python-guide.org/starting/installation/) and pip3
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
* [Chrome](https://www.google.com/chrome/) or [Firefox](https://www.mozilla.org/en-US/firefox/new/)

In a Terminal, run:

```
# Grab the code
git clone https://olivif@bitbucket.org/olivif/avworkshop.git
cd avworkshop

# Run these to install all the python packages needed
pip3 install -r requirements.txt
python3 manage.py runserver
```

You should see something like this (Ignore any warnings about database migrations):
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Note: You can use a python virtual environment if you don’t want to pollute your global setup. But you don’t have to.

## Workshop:02 – Download video (10 mins)
Manifest URL - http://www.bok.net/dash/tears_of_steel/cleartext/stream.mpd

Download video (add the code in player.html script tag)
BaseURL + representationId + segmentId 

Notes:
* Pick one representation for now 
* Segment ids are sequential, for this piece of content we have 245 segments, but download as many as you want (more than 1 )
* Make sure you get ArrayBuffer responses ( you can do this by printing the response of the http request and see an ArrayBuffer type)
* Open the developer tools network tab and observe


## Workshop:03 - Open a MediaSource (10 mins)
1. Create a MediaSource instance 
2. Link the media source instance to the video element on the page
3. Hook onto the MediaSource open event 
4. Make sure the MediaSource opens (add a console.log in the event handler)

https://developer.mozilla.org/en-US/docs/Web/API/MediaSource


## Workshop:04.1 - Play video (10 mins)
1. Feeding the init fragment 
2. Add a video source buffer 
3. Append the init fragment 

Notes:
If you’ve done everything correctly, you should see the duration of the video update (since now we have metadata)

https://developer.mozilla.org/en-US/docs/Web/API/SourceBuffer

## Workshop:04.2 - Play video (10 mins)
1. Appending video fragments
2. Add an event listener for updateend event
3. Append the video we downloaded previously in the updateend handler
4. Call play programmatically, or press play once on the page


## Workshop:05 - Play audio (15 mins)
Pretty much the same as we did for video


## Workshop:06 – Design adaptive quality levels (15 mins)
1. Now we’re playing a fixed quality level, but what if our bandwidth is lower than the quality we picked? What if our bandwidth fluctuates while we are watching the video? 
2. Design an adaptive quality level detection
3. Start with the lowest quality
4. Get some measure of how fast we are downloading and increase/decrease the quality level based on that
5. No need to write code for this one, but think about how you would do it and what information you need to keep track of.
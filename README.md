Content Page 
1. Web automation  mini project
2. Automation mini project 

-----------------------------
1. Web automation  mini project

Just want to share a web automation  mini project during my Bootcamp learning: 

The task of the mini project is about to do a automation of web-scarping a website that you like.

Then I choose to do web-scarping in some post of Reddit r/wallstreetbets.

And after 1 full day trying and half day for debug ,  I succeeded ! 

-----------------------------

There are two versions , one is simple ver , which contains a simple post with fews comments to web-scrape 

Another one is the more complex version, which is a Daily Discussion Thread of May 27 , 2022 , contains over 13k comments 

-----------------------------

Major challenge : 

 1. There are over 13k comments on this thread , and at first it only shows around 180 comments 
 2. However , the button is in the middle of the page , so you need a function to locate where it is to press
 3. The time loading of the webpage  is quite long , so the scroll down function sometimes need takes 3-4 times 
 
-----------------------------

How did I solve it : 

Refer to 1. challenge , as I need to remote a browser to click a button to show more comments. I use css selector to locate where the “see more replies”  button is and automate to click it

Refer to 2. challenge , I Google a function called “.location_once_scrolled_into_view”. Which is therefore useful to scroll down to specific location if I use css selector to find the element I want first (and I set the -4 comments of the thread) 

Refer to 3. challenge , just need the try except to let the function loop when it succeed to locate the -4 comments of the thread , however still finding way to solve the loop time become so slow after the 500th loop 

----------------------------- 

Reason of choosing this project  : 

Mainly For fun ! Haha!

But seriously , as a previous sociological researcher , the discussion in the forum is always a way that people chatting and exchanging ideas. It will be a new way for researcher to use these Big Data to know and get some meaning of these discussion thread

-----------------------------

2. Automation mini project 

Want to share another automation mini project during my Bootcamp learning: 
This is about to remote a virtual computer to run your Python task,
and upload the result to the Google Sheets automatically.

-----------------------------

Here is the Python task I set:  
to upload the result of my designed Options Calculator each month to Google Sheets 
The main reason to do this is simple: 
for presenting my result automatically for every time I run this python script to somewhere public 
without letting people seeing my source code (as it is a Business secret , haha!)

-----------------------------

Application of this project : 
You can use the Flask to do the whole Automation routine remotely 
even no need to start your own computer , 
this actually helps a lot 
when you want to collect data or update some data automatically every hour every day in many fields such as research and financial industry.


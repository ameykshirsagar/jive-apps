jive-apps
=========

Jive Apps - Offline web applications for Debian based Linux written in HTML5 

This was the conceptual implementation of fullscreen apps like Windows 8 using pywebkitgtk library in Ubuntu & Linux Mint. The webkit version it was using when I tested it back an year ago was 0.8. But it had supported pretty nice features like location, video, audio, canvas etc.

How to test?

1. Install pywebkitgtk on your machine. for that you need atleast 2.7 for python. Also install pygtk as the provide gtk bindings through python
2. Copy the contents of support in home folder. Open full.py in text editor. Browse to this line "view.open('file:///home/<username>/support/index.html')". Put your username in place of <username> & save it.
3. Type "cd support" in terminal.
4. Now type "python full.py"
5. Voila it will start running!!. To exit the app press ` (the key above tab and bellow escape)

Why build it?

I am quite attracted by the concept of Phonegap where it makes sure that the end-developer doesn't need to worry about modifying the native core of the app and concentrate on HTML/JS/CSS app. Also I wanted to try the new Windows 8 frameless fullscreen app concept in linux so I tried some of my luck and got a fullscreen app running HTML5 web app. With a decent UI framework we can make our own UI. Go ahead and try some of your luck and try making an offline app without using a local server.

In case of queries mail me at 

hansolo.amey@gmail.com

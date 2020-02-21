## Description

I've noticed a lot of people prepend their hints with "User:" or "Root:", so i wrote this very basic python script in one evening. It has some quirks and it's not gonna win a beauty contest, but it does the trick if you're looking for some quick hints on a specific box. 

Basically you have to feed a HackTheBox forum URL to this script, and it will look through every available page for comments from people that post hints for user and/or root.

It looks for the following contents in a comment (case insensitive):

* root:
* root :
* user:
* user :

For every hit, it will put the corresponding comment in an array, and then print the array on screen for both user and root hints.

I hope it helps you in finding useful hints! :)

## Help
```
Usage: python htbhints.py [URL]
Example: python htbhints.py https://forum.hackthebox.eu/discussion/2427/traverxec
PARAMETERS
  -h/--help: Print this help.
```

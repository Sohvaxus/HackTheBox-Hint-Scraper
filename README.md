
## TODO
* Remove duplicate comments -> this probably due to people quoting older comments
* Reduce false positives

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

## Requirements
* requests
```
# Python2
pip install requests
# Python3
pip3 install requests
```
This script is compatible with Python2 and Python3.

## Help
```
Usage: python htbhints.py [URL]
Example: python htbhints.py https://forum.hackthebox.eu/discussion/2427/traverxec
PARAMETERS
  -h/--help: Print this help.
```

## Example output
```
root@pwnux:~/Documents# python htbhints.py https://forum.hackthebox.eu/discussion/2630/nest
USER HINTS
----------
1. After finding the 1st user and the interesting files, finding the source is not that trivial, to me it was trial and error." />
2. Don't worry about poppin' shellz, that's not happening until root. Read everything carefully. If you think a room is too dark to go in, keep going! (But careful reading might get you your flashlight). The last step to user requires some skills that hide in the author's name.

ROOT HINTS
----------
1. It will be in front of you, read it and read it. Jump to the high port and explore, it will give you what you need to finish the box.
2. The file you find is obviously interesting, but where are Are Dis Stuff?? Once you got access to the service, you unlock some cool functionality. Don't stray too far - and don't forget what you've seen. Combine this with what you had before and profit!
3. try different decompilers!
4. over complicated the entire process thinking that i was looking for a hidden file that i couldn't find, i was convinced that i didn't know how to enumerate smb. Finally decided to throw my notes away and approach it like any other box . user and root came within an hour of each other.
```

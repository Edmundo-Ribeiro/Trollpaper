# TrollPaper
TrollPaper is a program to run in some friend's computers and have fun while they get unusual wallpapers periodically.

## Modules
For this project the folloing python modules whore used
* urllib.request
* ctypes
* os
* sys
* getpass
* pyinstaller

## Features
The program uses a list of pre selected images links to randomly download and set it as wallpaper.
Besisdes that, it initialize a schedule taks - in the windows task scheduler - that start the program every 2 hours.
It also delete itself from the directory where it was first ran and copy itself to the windows program startup folder.

## How to use
You can just download the .exe file and run the program in your friend's pc by double click on it. The program will set an awesome wallpaper and delete itself from the folder that you executed it.

To make some changes in the souce code, you can download the trollpaper.py file. After complete the changes you can convert the file into a .exe version by running pyinstaller -F -w trollpaper.py in the comand line (__if you have pyinstaller in your machine__). 

## Preview


### To do
- [ ] Make possible to insert new links easily
- [ ] Create the .exe file from the .py one
- [ ] Make a ubunto compatible version
- [ ] Place a personalized icon

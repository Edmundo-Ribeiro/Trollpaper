# TrollPaper
TrollPaper is a program to run in some friend's computers and have fun while they get unusual wallpapers periodically.

## Modules
For this project the following [pip]() modules were used
* urllib.request
* ctypes
* os
* sys
* getpass
* pyinstaller

## Features
The program uses a list of pre selected image links to randomly download them and set them as wallpaper.
Besisdes that, it initializes a scheduled task - in the windows task scheduler - which starts the program every 2 hours.
It also deletes itself from the directory where it was first ran and copies itself to the windows program startup folder.

## How to use
You can just download the .exe file and run the program in your friend's PC by double clicking on it. The program will set an awesome wallpaper and delete itself from the folder that you executed it.

To make some changes in the source code, you can download the trollpaper.py file. After complete the changes you can convert the file into the `.exe` version by running `pyinstaller -F -w trollpaper.py` in the comand line (__if you have pyinstaller in your machine__). 

## Preview
(work in progres)


### To do
Check the TODO list [here](https://github.com/Edmundo-Ribeiro/wallpaper/issues/2).

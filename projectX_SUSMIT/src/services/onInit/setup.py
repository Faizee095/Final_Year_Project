import json
import os
import sys
from pathlib import Path
from src.services.startUp.startUp import main
import sys
from os import path



def onInit():
    if getattr(sys, 'frozen') and hasattr(sys, '_MEIPASS'):
        print('running in a PyInstaller bundle')
    else:
        print('running in a normal Python process')

    bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    pathD = path.join(bundle_dir, 'user-settings.json')

    print("path->",pathD)

    with open(pathD, "r") as json_file:
        print(json.load(json_file))

    while True:
        pass

    """ mydict = {}
    print("----------------------Hello--------------------")
    print("Welcome to Home Automation")
    user_name = input("Enter user name ")
    music_lib_path = input("Enter path to music library ")
    while (os.path.isdir(music_lib_path) != True):
        print("Please enter a valid library path ")
    emailId, password = input(
        "Enter emailId and password separated by space ").split(" ")
    print("We are good to go, you can modify settings later by calling configure to the assistant ")
    print("----------------------Initialized---------------")
    mydict["user-name"] = user_name
    mydict["emailId"] = emailId
    mydict["password"] = password
    mydict["music-library-path"] = music_lib_path

    path = Path(__file__).parent / \
        "../../subsidiaries/components/settings/user-settings.json"

    with open(path, 'w') as json_file:
        json.dump(mydict, json_file) """


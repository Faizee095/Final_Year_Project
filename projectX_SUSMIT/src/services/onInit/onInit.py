import json
import os
import sys
from pathlib import Path


def onInit():
    frozen = 'not'
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    print('we are', frozen, 'frozen')
    print('bundle dir is', bundle_dir)
    print('sys.argv[0] is', sys.argv[0])
    print('sys.executable is', sys.executable)
    print('os.getcwd is', os.getcwd())

    # Actual Code
    mydict = {}
    print("\n----------------------Hello--------------------\n")
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

    path = bundle_dir+"\\user-settings.json"

    with open(path, 'w') as json_file:
        json.dump(mydict, json_file)

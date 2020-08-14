import json
import os
import sys
from pathlib import Path
from src.services.support.helper import clear_screen, get_path


def allGood():
    bundle_dir = get_path()

    # Actual Code
    print("\n----------------------Hello--------------------\n")
    print("Welcome to Home Automation")

    with open(
        # bundle_dir + "\\..\\..\\subsidiaries\\components\\settings\\user-settings.json"
        bundle_dir + "\\user-settings.json",
        "r",
    ) as f:
        user_data = json.load(f)
    if user_data["user-name"] != None:
        print("Launching application")
        clear_screen()
        return True
    else:
        return False


def save_user_details(user_name, emailId, password, music_lib_path):
    mydict = {}
    print("----------------------Initialized---------------")
    mydict["user-name"] = user_name
    mydict["emailId"] = emailId
    mydict["password"] = password
    mydict["music-library-path"] = music_lib_path

    path = (
        # get_path() + "\\..\\..\\subsidiaries\\components\\settings\\user-settings.json"
        get_path()
        + "\\user-settings.json"
    )
    with open(path, "w") as json_file:
        json.dump(mydict, json_file)


def onInit():
    bundle_dir = get_path()
    path = sys._MEIPASS + "\\user-settings.json"

    # Actual Code
    mydict = {}
    print("\n----------------------Hello--------------------\n")
    print("Welcome to Home Automation")

    with open(sys._MEIPASS + "\\user-settings.json", "r") as f:
        user_data = json.load(f)
    if user_data["user-name"] != None:
        print("Launching application")
        clear_screen()
        return
    else:
        user_name = input("Enter user name ")
        music_lib_path = input("Enter path to music library ")
        while os.path.isdir(music_lib_path) != True:
            print("Please enter a valid library path ")
        emailId, password = input(
            "Enter emailId and password separated by space "
        ).split(" ")
        print(
            "We are good to go, you can modify settings later by calling configure to the assistant "
        )
        print("----------------------Initialized---------------")
        mydict["user-name"] = user_name
        mydict["emailId"] = emailId
        mydict["password"] = password
        mydict["music-library-path"] = music_lib_path

        with open(path, "w") as json_file:
            json.dump(mydict, json_file)

    clear_screen()

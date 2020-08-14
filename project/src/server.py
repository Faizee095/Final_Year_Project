import eel
from src.services.startUp import startUp
import logging
import time
import pythoncom
from src.services.onInit.setup import save_user_details, allGood
from src.services.support import helper
import gevent

context = None


def start():
    eel.init("web")
    all_good = checkAllGood()
    if all_good == "page One":
        eel.start("active.html")
    else:
        eel.start("main.html")
    global context
    context.kill()
    logging.info(
        "Thread %s: finishing",
        "Main process for voice assisstant died due to window closing",
    )


@eel.expose
def get_user_details(user_name, email_id, password, music_library_path):
    print("received user name :", user_name)
    print("received email name :", email_id)
    print("received password :", password)
    print("received music path :", music_library_path)
    save_user_details(user_name, email_id, password, music_library_path)
    return "Gotcha !"


@eel.expose
def kickstart_console():
    return


@eel.expose
def voip():
    pythoncom.CoInitialize()
    logging.info("Thread %s: starting", "Calling main")
    global context
    context = gevent.spawn(startUp.main)
    context.start()
    logging.info("Thread %s: starting", "Started voice assistant")


@eel.expose
def stop_voip():
    print("current value ", helper.global_status_main)
    set_value()
    global context
    context.kill()
    logging.info("Thread %s: finishing", "Main process for voice assisstant died")


def set_value():
    helper.set_global_main_value(False)


def checkAllGood():
    result = allGood()
    if result == True:
        return "page One"
    else:
        return "page Two"


if __name__ == "__main__":
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    start()

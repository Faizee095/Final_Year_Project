from os import system, name
import sys
import os

global_status_main = True


def set_global_main_value(value):
    global global_status_main
    global_status_main = value


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def get_path():
    frozen = "not"
    if getattr(sys, "frozen", False):
        # we are running in a bundle
        frozen = "ever so"
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    print("we are", frozen, "frozen")
    print("bundle dir is", bundle_dir)
    print("sys.argv[0] is", sys.argv[0])
    print("sys.executable is", sys.executable)
    print("os.getcwd is", os.getcwd())
    return bundle_dir

from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
from src.services.support.helper import get_path
import json


def add_contacts(base_path):
    path = base_path + "\\MyContacts.json"
    with open(path, "r") as f:
        data = json.load(f)
    phone_data = data["phones"]

    VoiceEngine.getVoice("May I know the name of contact ?")
    name = SpeechRecogReg().lower()

    if name != None:
        VoiceEngine.getVoice("What is " + name + "'s contact number?")
        try:
            number = SpeechRecogReg()
            number_as = int(number)
        except:
            print("Not a number")
            return

        entry = {name: number}
        phone_data.update(entry)
        data.update(phone_data)

        with open(path, "w") as json_file:
            json.dump(data, json_file)

        VoiceEngine.getVoice("Phone Contact added successfully !")


def add_email_Contact(base_path):
    VoiceEngine.getVoice("May I know the name of contact ?")
    name = SpeechRecogReg().lower()

    if name != None:
        VoiceEngine.getVoice("What is " + name + "'s mail id?")
        mail = SpeechRecogReg()

        VoiceEngine.getVoice("Mail Contact added successfully !")


def change_music_library(base_path):
    VoiceEngine.getVoice("Please enter the new music library location?")
    music_lib_path = input("Enter location")


def change_user_name(base_path):
    VoiceEngine.getVoice("Please enter the new user name.")
    user_name = input("Enter user name")


def configuration():
    base_path = get_path()

    VoiceEngine.getVoice("Which setting do you want to configure?")
    choice_answer = SpeechRecogReg()

    if "email" or "mail" in choice_answer:
        add_contacts(base_path)
    elif "phone" in choice_answer:
        add_email_Contact(base_path)
    elif "music" or "library" in choice_answer:
        change_music_library(base_path)
    elif "user" or "name" in choice_answer:
        change_user_name(base_path)

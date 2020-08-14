from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import (
    SpeechRecogInit,
    SpeechRecogReg,
)
from src.services.actionDecider.actionDecider import ActionDecider
from src.services.support import helper
from src.subsidiaries.components.FaceRecognitionSystem import detector
import threading
from datetime import datetime
import eel


def main():
    lastSeen = datetime.now()
    commands = [
        "search google",
        "search youtube",
        "email",
        "message",
        "play music",
        "turn light on",
    ]

    t = threading.Thread(target=detector.detector)
    t.setDaemon(True)
    t.start()

    VoiceEngine()
    ActionDecider()

    eel.start_listening()
    VoiceEngine.getVoice("Welcome home")
    print("We are here")
    while helper.global_status_main == True:
        # print("code reached below point x 1")
        textForm = SpeechRecogInit()
        # print("code reached below point")
        if "Friday" in textForm:
            # eel.stop_listening()

            eel.show_info("Hi Boss How can I help You?")
            VoiceEngine.getVoice("Hi Boss! How can I help you ?")
            textForm = SpeechRecogReg()

            if textForm != "Invalid":
                value = ActionDecider.decideTakeAction(textForm)
                if value == 1:
                    break

        currentTime = datetime.now()

        if (currentTime - lastSeen).seconds > 20:
            if detector.active_event_list != []:
                print("Events found = ", detector.active_event_list)

                while detector.active_event_list != []:
                    event = detector.active_event_list.pop()
                    print("Event conclude = ", detector.active_event_list)
                    eel.show_info(event)
                    VoiceEngine.getVoice(event)

        # eel.sleep(0.05)
        # eel.sleep(1)
        eel.sleep(0.05)
    res = t.join()
    return


""" main() """

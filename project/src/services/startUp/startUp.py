from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogInit, SpeechRecogReg
from src.services.actionDecider.actionDecider import ActionDecider


def main():
    commands = ["search google", "search youtube",
                "email", "message", "play music", "turn light on"]

    VoiceEngine()
    ActionDecider()
    while True:
        textForm = SpeechRecogInit()
        if "Friday" in textForm:
            VoiceEngine.getVoice("Hi Boss! How can I help you ?")
            textForm = SpeechRecogReg()

            if (textForm != "Invalid"):
                value = ActionDecider.decideTakeAction(textForm)
                if value == 1:
                    break


""" main() """

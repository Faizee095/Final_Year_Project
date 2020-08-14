from datetime import date
import time
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
import eel


def timedate():
    today = date.today()
    t = time.localtime()
    current_time = time.strftime("%I:%p:%M", t)
    print(today)

    d2 = str("today is"), today.strftime("%B %d, %Y")

    VoiceEngine.getVoice(current_time)
    eel.show_info(d2)
    VoiceEngine.getVoice(d2)

import speech_recognition as sr
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine


def SpeechRecogInit():
    text = ""
    r1 = sr.Recognizer()
    # r1.dynamic_energy_threshold = True
    """ r1.energy_threshold = 400 """
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source)
        print("wake em up")
        audio = r1.listen(source)
        print("Yes recog is problematic")
        try:
            text = r1.recognize_google(audio)
        except sr.UnknownValueError:
            text = ""
            # VoiceEngine.getVoice("I am sorry I am having issues")
        except sr.RequestError as e:
            VoiceEngine.getVoice("I am sorry I am experiencing connectivity issues")
            text = ""
        finally:
            return text


def SpeechRecogReg():
    text = ""
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source)
        print("Give command")
        audio = r1.listen(source)
        try:
            text = r1.recognize_google(audio)
        except sr.UnknownValueError:
            VoiceEngine.getVoice("I am sorry I could not understand the audio")
            return "Invalid"
        except sr.RequestError as e:
            VoiceEngine.getVoice("I am sorry I am experiencing connectivity issues")
            return "Invalid"
        finally:
            return text

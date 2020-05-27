import speech_recognition as sr
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine


def SpeechRecogInit():
    text = ""
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("wake em up")
        audio = r1.listen(source)
        try:
            text = r1.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            VoiceEngine.getVoice(
                "I am sorry I am experiencing connectivity issues")
            text = ""
        finally:
            return text


def SpeechRecogReg():
    text = ""
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Give command")
        audio = r1.listen(source)
        try:
            text = r1.recognize_google(audio)
        except sr.UnknownValueError:
            VoiceEngine.getVoice("I am sorry I could not understand the audio")
            return "Invalid"
        except sr.RequestError as e:
            VoiceEngine.getVoice(
                "I am sorry I am experiencing connectivity issues")
            return "Invalid"
        finally:
            return text

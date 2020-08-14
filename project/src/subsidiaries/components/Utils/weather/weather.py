# Weather
import requests
from pprint import pprint
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
import eel


def getWeatherData():
    print("speak")
    VoiceEngine.getVoice("which City you want to search")

    id1 = SpeechRecogReg()
    eel.show_info(id1)
    c = print("You said ", id1)

    # try - except block
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=75eeb1def22ad1b37ad95298b918695c&units=metric".format(
            id1
        )
        res = requests.get(url)
        data = res.json()
        temp = str("The temperature is:"), data["main"]["temp"], str("degree celcius")
        description = str("It is"), data["weather"][0]["description"]

        """ print('Temperature : {} degree celcius'.format(temp))
        print('Description : {}'.format(description)) """

        VoiceEngine.getVoice(temp)
        VoiceEngine.getVoice(description)
        eel.show_info(description)
    except expression as identifier:
        VoiceEngine.getVoice("No such place found")
        eel.show_info("No such place found")

    return

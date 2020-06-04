"""
Current mode: fetches top 20 headlines with descriptions and in depth contents.
Options: Set news source option,
         Set origin country,
         Search news articles that mention a specific topic/keyword
         fetch and filter by published dates,
         filter by category
         retrieves url, images as well, can directly show on the 
         phone via push messages, etc if it were little more smart. (Seemless sharing of data)
"""
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine
from src.subsidiaries.components.Utils.speech.speechText import SpeechRecogReg
import requests


def handleResponse(response):
    if (response["status"] == "ok"):
        top_articles = response["articles"]
        print("Number of trending articles->", len(top_articles))
        for i in top_articles:
            print("Source: ", i["source"]["name"])
            print("headline: ", i["title"])
            VoiceEngine.getVoice(i["title"])
            # ask if details are required and print i["description"]
            VoiceEngine.getVoice(i["description"])

            # ask if in depth details are required and print i["content"]
            ask_for_details = SpeechRecogReg()
            if "get details" in ask_for_details:
                VoiceEngine.getVoice(i["content"])
            if "stop" in ask_for_details:
                break

            # return ok
    else:
        VoiceEngine.getVoice(
            "I think there is some error. Should I try again ?")
        attempt = SpeechRecogReg()
        if "Yes" in attempt or "try again" in attempt:
            return "1"
        return "0"
        # some error wanna try again ? or better try later ?
        # return 1 for try again, 0 for try later


def fetchQueryNews(query):
    status = "1"
    while status == "1":
        url = (
            "http://newsapi.org/v2/everything?"
            "q=" + query + "&"
            "from=2020-05-31&"
            "sortBy=popularity&"
            "apiKey=a6fca971210a42aa9cd331f75d95bb65"
        )
        response = requests.get(url).json()
        status = handleResponse(response)
        if (status != "1"):
            break


def fetchDailyNews():
    status = "1"
    while status == "1":
        url = (
            "http://newsapi.org/v2/top-headlines?"
            "country=in&"
            "apiKey=a6fca971210a42aa9cd331f75d95bb65"
        )
        response = requests.get(url).json()
        response = requests.get(url).json()
        status = handleResponse(response)
        if (status != "1"):
            break


def newsFeed():
    VoiceEngine.getVoice("Sir, what would you like to hear ?")
    wish = SpeechRecogReg().lower()

    if "headlines" or "headline" in wish:
        fetchDailyNews()
    else:
        fetchQueryNews(wish)
    return

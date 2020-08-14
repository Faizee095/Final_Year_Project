import requests
from src.subsidiaries.components.Utils.speech.textSpeech import VoiceEngine

v = VoiceEngine()

# Google Custom Search API = AIzaSyCQqU3_f7wYaRrjdKTDUv3SZYaehSUaT9Y
api_key = "AIzaSyCQqU3_f7wYaRrjdKTDUv3SZYaehSUaT9Y"
custom_search_engine_id = "000136155493922381280:oylu78ni5ik"
query = "height of Qutub Minar"
url = (
    "https://www.googleapis.com/customsearch/v1?key="
    + api_key
    + "&cx="
    + custom_search_engine_id
    + "&q="
    + query.replace(" ", "+")
)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
res = (requests.get(url=url, headers=headers)).json()
ans = res["items"][1]["snippet"]
print(ans)
v.getVoice(ans)

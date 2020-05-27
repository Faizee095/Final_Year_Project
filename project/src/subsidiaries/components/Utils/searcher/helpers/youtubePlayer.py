# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 03:46:29 2019
@author: Sumit Kumar Singh
"""
import requests
import json


def playOnYoutube(ques):
    URL = (
        "https://www.googleapis.com/youtube/v3/search?part=id&q="
        + ques.replace(" ", "+")
        + "&type=video&key=AIzaSyCQqU3_f7wYaRrjdKTDUv3SZYaehSUaT9Y"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    res = str(requests.get(url=URL, headers=headers).text)
    res = json.loads(res)
    # print(res)

    ans = "http://youtube.com/watch?v=" + res["items"][1]["id"]["videoId"]

    return ans


# print(playOnYoutube('radhe radhe'))

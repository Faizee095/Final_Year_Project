import requests

def getGoogleAnswer(ques):
    URL = "https://www.google.com/search?q="+ques.replace(' ','+')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    res = str(requests.get(url=URL,headers=headers).text)

    # f = open('response.html','w')
    # f.write(res)
    # f.close()

    # print(res)

    index = res.index('role="heading"')
    res = res[index+len("role='heading'"):]
    # print(len(res1))

    index = res.index('role="heading"')
    res = res[index:]



    index = res.find('>')
    res = res[index+1:]

    ans = ""

    while(len(ans)==0):
        index = res.find('>')
        res = res[index+1:]

        index = res.index('<')
        ans += res[:index]

    return ans

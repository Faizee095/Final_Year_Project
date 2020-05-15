import requests
import json

def sender(number,msg):
            URL = 'http://www.way2sms.com/api/v1/sendCampaign'

            # get request
            def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
              req_params = {
              'apikey':apiKey,
              'secret':secretKey,
              'usetype':useType,
              'phone': phoneNo,
              'message':textMessage,
              'senderid':senderId
              }
              return requests.post(reqUrl, req_params)

            # get response
            response = sendPostRequest(URL, '7ZRA0OQ1COMUGOALBRKQTIFOMQSS3FNL', '7A3HVUBJLY4LNZJF', 'stage', number, 'x', msg )
           
  

sender("8709442967" , "Somebody is there . . .")
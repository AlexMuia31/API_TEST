import json, requests, base64
import logging, urllib3
import sys
import verboselogs
from http.client import HTTPConnection
import time
from requests.auth import HTTPBasicAuth
from datetime import datetime


start_time = time.time()
log= logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

HTTPConnection.debuglevel = 1



class MpesaC2bCredential:
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    print ("-------MpesaAccessToken------")
    print(r.text)
    print(r)
    print ("-------validated_mpesa_access_token------")
    print (validated_mpesa_access_token)
   
class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

    print("------online_password------")
    print (online_password)
    print ("------------------------------------------------------------")

def pull_transaction():
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/pulltransactions/v1/query"
    headers = {"Authorization": "Bearer %s" % access_token}

    print(access_token)

    request = {
        "BusinessShortCode": '174379',
        "StartEnd": "2021-04-15 8:36:00",
        "EndDate": "2021-04-16 10:10:000",
        "OffSetValue": "0"
    }


    print(json.dumps(request))
    response = requests.post(api_url, json=request, headers=headers, verify=False)
    print (response.text)



print (pull_transaction())

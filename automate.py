import requests
import os

API = "https://sg-act-nap-api.hoyolab.com/event/luna/zzz/os/sign"
# Please check your cookies setting to change this. 
LTUID = os.environ['LTUID']
LTOKEN = os.environ['LTOKEN']

def main():
    cookies = {
        'ltoken': f'{LTOKEN}',
        'ltuid': f'{LTUID}'
    }
    payload = {
            'act_id': 'e202406031448091',
            'lang': 'en-us'
        }
    try:
        response = requests.post(API, cookies=cookies, json=payload)
        response.raise_for_status()
        response_message = response.json()
        if response_message['retcode'] == 0:
            print("Zenless Zone Zero Daily Check-in SUCCESS")
        elif response_message['retcode'] == -5003:
            print(response_message['message'])
        elif response_message['retcode'] == -100:
            print("Your cookies has expired. Please update your cookies.")
    except requests.exceptions.RequestException as e:
        print("Request Error occured ", e)

if __name__ == "__main__":
    main()
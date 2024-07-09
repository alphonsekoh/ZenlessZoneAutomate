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
    try:
        response = requests.post(API, cookies=cookies)
        response.raise_for_status()
        response_message = response.json()
        if response_message['retcode'] == 0 and response_message['message'] == 'OK':
            print("Zenless Zone Zero Daily Check-in SUCCESS")
        elif response_message['retcode'] == -400005:
            print(response_message['message'])
        elif response_message['retcode'] == -100:
            print("Your cookies has expired. Please update your cookies.")
    except requests.exceptions.RequestException as e:
        print("Request Error occured ", e)

if __name__ == "__main__":
    main()
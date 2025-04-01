import requests
import os

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']
TL_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def sendMessageToBot(message):
   try:
      requests.post(TL_URL, json={'chat_id': CHAT_ID, 'text': message})
   except Exception as e:
      print(e)

def check_text_in_page(url, text_to_find):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if text_to_find in response.text:
            #sendMessageToBot("TEST")
            return True
        else:
            sendMessageToBot("TRAIN TICKET RELEASEE")
            return False
    
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return False

url = "https://www.siciliaexpress.eu"
text_to_find = "Coming soon"
check_text_in_page(url, text_to_find)

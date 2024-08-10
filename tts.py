from constants import ttsURL

import urllib.parse
import requests
import re



def generateTTS(text, voice):
    '''
    This is a helper function that is used for generating and playing an AI message. It also does some small sanitizing to the TTS speech before it gets sent.
    Takes in the text to get translated, and what voice to use.
    Returns the response of the TTS service
    '''
    sanitizedText = re.sub(r'\[.*\] ', '', text)
    payload = f"text_input={urllib.parse.quote(sanitizedText)}&text_filtering=standard&character_voice_gen={voice}&narrator_enabled=false&narrator_voice_gen=male_01.wav&text_not_inside=character&language=en&output_file_name=tempOutput&output_file_timestamp=true&autoplay=true&autoplay_volume=0.8"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", ttsURL, headers=headers, data=payload)
    return response.text


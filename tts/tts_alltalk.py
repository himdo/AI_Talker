from constants import ttsURL

import urllib.parse
import requests
import re
import json

def generateTTS(text: str, voice: str) -> str:
    '''
    Generates TTS using AllTalk
    :param text: The text to be converted to speech
    :param voice: The voice to be used for the TTS
    :return: The path to the generated audio file
    '''
    sanitizedText = re.sub(r'\[.*\] ', '', text)
    payload = f"text_input={urllib.parse.quote(sanitizedText)}&text_filtering=standard&character_voice_gen={voice}&narrator_enabled=false&narrator_voice_gen=male_01.wav&text_not_inside=character&language=en&output_file_name=tempOutput&output_file_timestamp=true&autoplay=false&autoplay_volume=0.8"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", ttsURL, headers=headers, data=payload)
    fileLocation = json.loads(response.text)['output_file_path']
    print (fileLocation)
    return fileLocation
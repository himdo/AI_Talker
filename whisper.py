from constants import translationURL
from ais import aiLists

import requests
from colorama import Fore
import os
import json



def __translateFile(fileLocation):
    '''
    This is purely a helper function. It takes in a file location and spits out the text according to whisper.cpp
    '''
    payload = {}
    files=[
    ('file',('file.wav',open(fileLocation,'rb'),'audio/wav'))
    ]
    headers = {}
    response = requests.request("POST", translationURL, headers=headers, data=payload, files=files)
    return json.loads(response.text)['text']

def __TranslateFilePathAndClean(filepath):
    '''
    This is purely a helper function. It takes a file path, sends it to be translated and deletes the file.
    This also spits out the text into the console and returns the text.
    '''
    translatedText = __translateFile(filepath)
    os.remove(filepath)
    print(f"{Fore.BLUE}{translatedText}")
    return translatedText

def TranslateFilePathAndSendToLLM(filepath):
    '''
    This takes a filepath, translates and cleans it then sends that to all AIs.
    '''
    text = __TranslateFilePathAndClean(filepath)
    newMessage = {"role":"user", "content":text}
    for i in range(len(aiLists)):
        aiLists[i].addToLLM_Messages(newMessage)
    print(f"{Fore.GREEN} You can now choose who to talk")



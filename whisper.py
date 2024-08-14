from constants import translationURL
from ais import aiLists

import requests
from colorama import Fore
import os
import json



def __translateFile(fileLocation: str) -> str:
    '''
    This is purely a helper function. It takes in a file location and spits out the text according to whisper.cpp
    :param fileLocation: The location of the file to be translated
    :return: The translated text
    '''
    payload = {}
    files=[
    ('file',('file.wav',open(fileLocation,'rb'),'audio/wav'))
    ]
    headers = {}
    response = requests.request("POST", translationURL, headers=headers, data=payload, files=files)
    return json.loads(response.text)['text']

def __TranslateFilePathAndClean(filepath: str) -> str:
    '''
    This is purely a helper function. It takes a file path, sends it to be translated and deletes the file.
    :param filepath: The location of the file to be translated
    :return: The translated text
    '''
    translatedText = __translateFile(filepath)
    os.remove(filepath)
    print(f"{Fore.BLUE}{translatedText}")
    return translatedText

def TranslateFilePathAndSendToLLM(filepath: str):
    '''
    This takes a filepath, translates and cleans it then sends that to all AIs.
    :param filepath: The location of the file to be translated
    '''
    text = __TranslateFilePathAndClean(filepath)
    newMessage = {"role":"user", "content":text}
    for i in range(len(aiLists)):
        aiLists[i].addToLLM_Messages(newMessage)
    print(f"{Fore.GREEN} You can now choose who to talk")



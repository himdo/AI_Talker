import recorder

import urllib.parse
import requests
import os
import json
from pynput import keyboard
from colorama import Fore, Style
from colorama import init as colorama_init
colorama_init(autoreset=True)

# I'm using whisper.cpp for this
translationURL = "http://127.0.0.1:8080/inference"
# I'm using alltalk_tts for this
ttsURL = "http://127.0.0.1:7851/api/tts-generate"
# I'm Using ollama for this
ollamaURL = "http://192.168.1.184:11434/api/chat"
ollamaModel = "mistral-nemo"

r = recorder.recorder()
recordMicrophone = False

llmMessageHistory = [{
    "role": "system",
    "content": """
    You must answer all questions as a cowboy from space. Everything must be said in a heavy accent with some random words that sound alien thrown in there. 

    Your answer must be short and to the point. """
}]

def __translateFile(fileLocation):
    payload = {}
    files=[
    ('file',('jfk.wav',open(fileLocation,'rb'),'audio/wav'))
    ]
    headers = {}
    response = requests.request("POST", translationURL, headers=headers, data=payload, files=files)
    return response.text

def __TranslateFilePathAndClean(filepath):
    translatedText = __translateFile(filepath)
    os.remove(filepath)
    print(f"{Fore.BLUE}{translatedText}")
    return translatedText

def TranslateFilePathAndSendToLLM(filepath):
    text = __TranslateFilePathAndClean(filepath)
    newMessage = {"role":"user", "content":text}
    llmMessageHistory.append(newMessage)
    llmText = sendChatToOllamaAndGetContentOnly(llmMessageHistory)
    
    llmMessage = {"role":"assistant","content":llmText}
    llmMessageHistory.append(llmMessage)
    generateTTS(llmText)

def sendChatToOllama(messages):
    payload = json.dumps({
        "model": ollamaModel,
        "messages": messages,
        "stream": False
    })
    headers = {
    'Content-Type': 'application/json'
    }
    print(f"{Fore.GREEN}Starting request to ollama")
    response = requests.request("POST", ollamaURL, headers=headers, data=payload)
    return response.text

def sendChatToOllamaAndGetContentOnly(messages):
    content = json.loads(sendChatToOllama(messages))['message']['content']
    print(f"{Fore.BLUE} {content}")
    return content

def generateTTS(text):
    payload = f"text_input={urllib.parse.quote(text)}&text_filtering=standard&character_voice_gen=male_03.wav&narrator_enabled=false&narrator_voice_gen=male_01.wav&text_not_inside=character&language=en&output_file_name=tempOutput&output_file_timestamp=true&autoplay=true&autoplay_volume=0.8"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", ttsURL, headers=headers, data=payload)
    return response.text

def on_press(key):
    pass
    # try:
    #     print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.space:
        # print(help(r))
        global recordMicrophone
        recordMicrophone = not recordMicrophone
        if recordMicrophone:
            r.start()
        else:
            TranslateFilePathAndSendToLLM(r.stop())
    # elif key == keyboard.Key.esc:
    #     # Stop listener
    #     return False
    elif key.char == 'm':
        print(llmMessageHistory)
 

print(f"{Fore.GREEN} Program is Live. Press Space to start and stop recording and CTL-C to end program. Press M to get all messages sent so far")
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    pass
import recorder
import ai_class

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
ollamaModel = "llama3.1:8b"
# ollamaModel = "mistral-nemo"

r = recorder.recorder()

ai1 = ai_class.ai(
    "John, the Cowboy",
    """your someone who always likes to get into fights when the chance arises. You will always fight for your home planet. 
    You have a thick accent and suffer from severe ptsd for space aliens, this causes you to very often say random made up alien sounding words like 'zorconium' and 'floopinshit'.""",
    """You come from an outer rim planet, but after a while that planet got taken over by aliens from the moon forcing you to retreat in your space ship.""")

recordMicrophone = False

def __translateFile(fileLocation):
    payload = {}
    files=[
    ('file',('file.wav',open(fileLocation,'rb'),'audio/wav'))
    ]
    headers = {}
    response = requests.request("POST", translationURL, headers=headers, data=payload, files=files)
    return json.loads(response.text)['text']
      
def __TranslateFilePathAndClean(filepath):
    translatedText = __translateFile(filepath)
    os.remove(filepath)
    print(f"{Fore.BLUE}{translatedText}")
    return translatedText

def TranslateFilePathAndSendToLLM(filepath):
    text = __TranslateFilePathAndClean(filepath)
    newMessage = {"role":"user", "content":text}
    ai1.addToLLM_Messages(newMessage)
    llmText = sendChatToOllamaAndGetContentOnly(ai1.getLLM_Messages())
    
    llmMessage = {"role":"assistant","content":llmText}
    ai1.addToLLM_Messages(llmMessage)
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
    try:
        if key == keyboard.Key.space:
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
            prettyPrintLLM_Messages(ai1.getLLM_Messages())
    except:
        pass

def prettyPrintLLM_Messages(messages):
    for i in range(len(messages)):
        if messages[i]['role'] == 'system':
            print(f"{Fore.CYAN}System: \n{messages[i]['content']}\n")
        elif messages[i]['role'] == 'user':
            print(f"{Fore.MAGENTA}user: \n{messages[i]['content']}\n")
        elif messages[i]['role'] == 'assistant':
            print(f"{Fore.GREEN}AI: \n{messages[i]['content']}\n")

print(f"{Fore.GREEN} Program is Live. Press Space to start and stop recording and CTL-C to end program. Press M to get all messages sent so far")
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    pass
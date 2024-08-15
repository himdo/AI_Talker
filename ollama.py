from ais import aiLists
from constants import ollamaModel, ollamaURL
from tts.tts_piper import generateTTS
from wav_player import wav_player
import json
import requests
from colorama import Fore

def sendIntroductionToAllAIs():
    '''
    This function should only be called once. It is used to introduce all AIs to each other and behave as a starting text.
    '''

    templateMessage = f"Hello All, you are about to begin an adventure. Today you are all gathered as a group of adventures, in your party you have "
    for i in range(len(aiLists)):
        templateMessage += f"\"{aiLists[i].getAI_Name()}\""
        if i < len(aiLists) -1:
            templateMessage += ", "
    templateMessage += ". Remember to always behave as your character and to never talk as anyone else."
    message = {"role":"user","content":templateMessage}
    for i in range(len(aiLists)):
        aiLists[i].addToLLM_Messages(message)

def generateAndTalkAI(ai: object):
    '''
    This Requests Ollama to generate text for the given AI.
    It will then save that message to all AIs.
    Finally it will generate and play the TTS of the AI.

    This is a primary function that runs.
    :param ai: The AI to generate and talk as.
    '''
    llmText = sendChatToOllamaAndGetContentOnly(ai)
    
    llmMessage = {"role":"user","content":llmText}
    for i in range(len(aiLists)):
        aiLists[i].addToLLM_Messages(llmMessage)
    wav_player().play_audio(generateTTS(llmText, ai.ai_voice))
    print(f"{Fore.GREEN}{ai.getAI_Name()} is done talking.")


def sendChatToOllamaAndGetContentOnly(ai_reference: object):
    '''
    This informs the user of what the AIs are doing when it is going to ollama.
    :param ai_reference: The AI to send to ollama
    :return: The content of the message from ollama
    '''
    print(f"{Fore.GREEN} {ai_reference.getAI_Name()} is thinking")
    content = json.loads(__sendChatToOllama(ai_reference.getLLM_Messages()))['message']['content']
    print(f"{Fore.BLUE} {content}")
    return content


def __sendChatToOllama(messages: list) -> str:
    '''
    This is a helper function that generates a payload and sends the request to ollama.
    It takes in all the messages from the AIs and returns new text
    :param messages: The list of messages to be sent to ollama
    :return: The response from ollama
    '''
    try:
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
    except Exception as e:
        print(f"{Fore.RED} Error: {e}")
        return json.dumps({"message": {"content": "Ollama is down"}})


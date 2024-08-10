from ais import aiLists
from ollama import generateAndTalkAI

from colorama import Fore
import random

def deleteLastLLMMessage():
    '''
    This is a function that removes the last message sent to all ai's and is useful when things go wrong.
    '''
    print(f"{Fore.RED} Deleting last LLM Message")
    for i in range(len(aiLists)):
        ai = aiLists[i]
        messages = ai.getLLM_Messages()
        messages = messages[:-1]
        ai.setLLM_Messages(messages)

def prettyPrintLLM_Messages(messages):
    '''
    This does some formatting to a list of messages to present the chat history in the terminal
    '''
    for i in range(len(messages)):
        if messages[i]['role'] == 'system':
            # print(f"{Fore.CYAN}System: \n{messages[i]['content']}\n")
            pass
        elif messages[i]['role'] == 'user':
            print(f"{Fore.MAGENTA}user: \n{messages[i]['content']}\n")
        elif messages[i]['role'] == 'assistant':
            print(f"{Fore.GREEN}AI: \n{messages[i]['content']}\n")

def idleChatBetweenAIs():
    '''
    Generate and talk as a random AI.
    '''
    generateAndTalkAI(aiLists[random.randrange(0,len(aiLists))])

def forceAIToTalk(ai_number):
    '''
    Forces a specific AI to talk, If the AI does not exist it will print an error to the screen.

    Takes in a Int.
    '''
    if (ai_number+1) > len(aiLists):
        print(f"{Fore.RED} AI: {ai_number} does not exist")
        return
    generateAndTalkAI(aiLists[ai_number])

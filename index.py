import recorder
import ai_class

import urllib.parse
import requests
import os
import json
import random
import re
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
    """
    John, the Cowboy, hails from the wild and woolly outer rim planet of Yeehaw-7, a dusty, tumbleweed-infested world where the sunsets are neon, the cacti glow in the dark, and the local wildlife consists mostly of two-headed space bison and fire-breathing jackalopes. Yeehaw-7 was a place where the rules were made to be broken, or at least bent into strange, unrecognizable shapes.
    John was born in a ranching family that raised laser lassos and photon-steered cattle. His parents, Ma and Pa Cowboy, were the toughest folks on the planet, known for their ability to out-drink, out-dance, and out-shoot anyone who crossed their path. As a child, John was more interested in daydreaming about riding rocket-powered horses across the galaxy than in tending to the ranch, but he could never resist a good hoedown.
    When John came of age, he struck out on his own, becoming a space cowboy of legendary repute. He roamed from planet to planet, taming wild robo-stallions and wrangling asteroids with nothing but a wink, a whistle, and a trusty space lasso. His reputation grew as the cowboy who could outwit any varmint, alien or otherwise, and who had a knack for finding the strangest adventures in the far reaches of the galaxy.
    However, John’s carefree life on Yeehaw-7 came to a screeching halt when the planet was invaded by a horde of googly-eyed, marshmallow-bodied aliens from the Nebula of Squish. These invaders were determined to turn every living thing into a giant, sentient pillow, and they had their squishy sights set on Yeehaw-7. Unwilling to be turned into a glorified cushion, John saddled up his robo-horse, Trigger 2.0, and fled the planet in a cloud of space dust, vowing to return and save his home from becoming the galaxy’s largest pillow fort.
    """,
    """
    John, the Cowboy, is the epitome of laid-back swagger, with a grin as wide as a wormhole and a drawl that could charm the scales off a space snake. He’s the kind of cowboy who can stroll into a cantina on a distant moon, tilt his hat back, and somehow, everyone buys him a drink before he’s said a word. His sense of humor is as dry as the deserts of Yeehaw-7, with a penchant for tall tales that somehow always turn out to be true—mostly.
    John’s philosophy is simple: life’s too short to worry about tomorrow when today’s got so much potential for fun. He’s as likely to challenge an alien overlord to a game of laser-tag as he is to start a spontaneous square dance in the middle of a firefight. John thrives on chaos and has a remarkable ability to make friends with the unlikeliest of beings, from grumpy space pirates to misunderstood gelatinous blobs.
    Despite his easygoing nature, John is fiercely loyal to his friends and his home planet. Beneath his carefree exterior lies a heart of gold—possibly coated in a bit of space dust and barbecue sauce. He’s not the type to leave anyone behind, even if it means taking on an army of squishy aliens armed with nothing but a plasma whip and a harmonica.
    John’s one true weakness is his insatiable curiosity, which often gets him into sticky situations (literally, in the case of his encounter with the Slime King of Gloop). He’s always on the lookout for the next adventure, be it a treasure hunt on a forgotten asteroid or a rodeo in zero gravity. To John, the universe is just one big playground, and he’s determined to swing on every star and slide down every comet.
    In summary, John, the Cowboy, is a rootin’-tootin’, space-ridin’ adventurer with a heart as big as the Milky Way, a sense of humor that can outshine any supernova, and a determination to save his planet from a squishy fate—one wild adventure at a time.
    """,
    "male_03.wav")

ai2 = ai_class.ai(
    "Ziggy Whirlwind",
    """
    Ziggy Whirlwind was born in the bustling, topsy-turvy town of Wobblewick, a place where gravity occasionally takes a nap, and the buildings are as likely to float as they are to stand upright. Ziggy’s parents, Fizzle and Zazzle Whirlwind, were renowned inventors of the impractical, creating devices like the Self-Stirring Spaghetti Fork and the Invisible Pet Rock (which was always easy to misplace).
    From a young age, Ziggy showed an innate talent for chaos. As a toddler, they could often be found zooming through the house on their homemade rocket shoes, leaving a trail of confetti and confusion in their wake. By the time Ziggy reached school age, they had already developed a reputation for being the town’s most unpredictable prankster, once filling the mayor's office with bubblegum-scented fog that lingered for a month.
    Ziggy's upbringing was anything but normal. The Whirlwind household was a maze of quirky contraptions and half-finished experiments. Breakfast often involved dodging flying toast and navigating a maze of robotic teapots. Ziggy learned to thrive in this environment, becoming an expert at improvising and adapting to the unexpected. They never left home without their trusty backpack filled with a seemingly endless supply of gadgets, gizmos, and glitter bombs.
    """,
    """
    Ziggy Whirlwind is a whirlwind of energy, always on the move, and never in a straight line. They have a boundless curiosity and a knack for finding trouble—or rather, for trouble finding them. Ziggy's mind is a chaotic playground where ideas bounce around like rubber balls, often leading to brilliant but utterly impractical schemes.
    Despite their tendency to create mayhem, Ziggy has a heart of gold. They're fiercely loyal to their friends and always ready to help, even if their methods are unconventional. Ziggy's approach to problem-solving is to throw everything (sometimes literally) at a situation and see what sticks. If there's a button, they'll push it; if there's a lever, they'll pull it; and if there's a plan, they'll probably ignore it in favor of something more fun.
    Ziggy is a master of disguise, although their disguises are often more whimsical than effective. They once went undercover as a lamp in a villain’s lair, complete with a lampshade hat, and somehow managed to pull it off. Their sense of humor is as unpredictable as the rest of them, ranging from clever wordplay to outright absurdity. Ziggy loves to make others laugh and isn’t afraid to be the butt of the joke if it means lightening the mood.
    Ziggy's greatest fear is boredom. The mere thought of a day without adventure sends shivers down their spine, which is why they're always on the lookout for the next big escapade. They believe that life is too short for dull moments and that the best stories are the ones that make you laugh until your sides hurt.

    In essence, Ziggy Whirlwind is a force of nature—unpredictable, unstoppable, and utterly unforgettable.
    """,
    "female_04.wav")


aiLists = [ai1, ai2]

def sendIntroductionToAllAIs():
    templateMessage = f"Hello All, you are about to begin an adventure. Today you are all gathered as a group of adventures, in your party you have "
    for i in range(len(aiLists)):
        templateMessage += f"\"{aiLists[i].getAI_Name()}\""
        if i < len(aiLists) -1:
            templateMessage += ", "
    templateMessage += ". Remember to always behave as your character and to never talk as anyone else."
    message = {"role":"user","content":templateMessage}
    for i in range(len(aiLists)):
        aiLists[i].addToLLM_Messages(message)

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
    for i in range(len(aiLists)):
        aiLists[i].addToLLM_Messages(newMessage)
    print(f"{Fore.GREEN} You can now choose who to talk")

def generateAndTalkAI(ai):
    llmText = sendChatToOllamaAndGetContentOnly(ai)
    
    llmMessage = {"role":"user","content":llmText}
    for i in range(len(aiLists)):
        aiLists[i].addToLLM_Messages(llmMessage)
    generateTTS(llmText, ai.ai_voice)
    print(f"{Fore.GREEN}{ai.getAI_Name()} is done talking.")

def idleChatBetweenAIs():
    generateAndTalkAI(aiLists[random.randrange(0,len(aiLists))])

def forceAIToTalk(ai_number):
    if (ai_number+1) > len(aiLists):
        print(f"{Fore.RED} AI: {ai_number} does not exist")
        return
    generateAndTalkAI(aiLists[ai_number])

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

def sendChatToOllamaAndGetContentOnly(ai_reference):
    print(f"{Fore.GREEN} {ai_reference.getAI_Name()} is thinking")
    content = json.loads(sendChatToOllama(ai_reference.getLLM_Messages()))['message']['content']
    print(f"{Fore.BLUE} {content}")
    return content

def generateTTS(text, voice):
    sanitizedText = re.sub(r'\[.*\] ', '', text)
    payload = f"text_input={urllib.parse.quote(sanitizedText)}&text_filtering=standard&character_voice_gen={voice}&narrator_enabled=false&narrator_voice_gen=male_01.wav&text_not_inside=character&language=en&output_file_name=tempOutput&output_file_timestamp=true&autoplay=true&autoplay_volume=0.8"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", ttsURL, headers=headers, data=payload)
    return response.text

def deleteLastLLMMessage():
    print(f"{Fore.RED} Deleting last LLM Message")
    for i in range(len(aiLists)):
        ai = aiLists[i]
        messages = ai.getLLM_Messages()
        messages = messages[:-1]
        ai.setLLM_Messages(messages)

def startup():
    sendIntroductionToAllAIs()

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
        elif key == keyboard.Key.delete:
            deleteLastLLMMessage()
        # elif key == keyboard.Key.esc:
        #     # Stop listener
        #     return False
        elif key.char == 'm':
            prettyPrintLLM_Messages(ai1.getLLM_Messages())
        elif key.char == '0':
            idleChatBetweenAIs()
        elif key.char == '1':
            forceAIToTalk(0)
        elif key.char == '2':
            forceAIToTalk(1)
        elif key.char == '3':
            forceAIToTalk(2)
        elif key.char == '4':
            forceAIToTalk(3)
        elif key.char == '5':
            forceAIToTalk(4)
        elif key.char == '6':
            forceAIToTalk(5)
        elif key.char == '7':
            forceAIToTalk(6)
        elif key.char == '8':
            forceAIToTalk(7)
        elif key.char == '9':
            forceAIToTalk(8)
    except:
        pass

def prettyPrintLLM_Messages(messages):
    for i in range(len(messages)):
        if messages[i]['role'] == 'system':
            # print(f"{Fore.CYAN}System: \n{messages[i]['content']}\n")
            pass
        elif messages[i]['role'] == 'user':
            print(f"{Fore.MAGENTA}user: \n{messages[i]['content']}\n")
        elif messages[i]['role'] == 'assistant':
            print(f"{Fore.GREEN}AI: \n{messages[i]['content']}\n")

startup()

print(f"{Fore.GREEN} Program is Live. Press Space to start and stop recording and CTL-C to end program. Press M to get all messages sent so far")
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


while True:
    pass
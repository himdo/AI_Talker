
from ollama import sendIntroductionToAllAIs
from keyboard_keys import listener

from colorama import Fore
from colorama import init as colorama_init
from wav_player import wav_player
colorama_init(autoreset=True)

def startup():
    '''
    This is the startup app.
    '''
    sendIntroductionToAllAIs()
    
    listener.start()

startup()

print(f"""
    {Fore.GREEN}Program is Live. 
    Press {Fore.CYAN}Space{Fore.GREEN} to start and stop recording
    Press {Fore.CYAN}CTRL-C{Fore.GREEN} to end program.
    Press {Fore.CYAN}M{Fore.GREEN} to get all messages sent so far
    Press {Fore.CYAN}1-9{Fore.GREEN} on number row to force trigger to AIs
    Press {Fore.CYAN}0{Fore.GREEN} to have random ai talk
    Press {Fore.CYAN}Delete{Fore.GREEN} to delete last message for all AIs
    """)

while True:
    pass
from whisper import TranslateFilePathAndSendToLLM
from ai_methods import deleteLastLLMMessage, prettyPrintLLM_Messages, idleChatBetweenAIs, forceAIToTalk
from ais import aiLists
import recorder

from pynput import keyboard

r = recorder.recorder()
recordMicrophone = False

def on_press(key):
    pass
    # try:
    #     print('alphanumeric key {0} pressed'.format(key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(key))

def on_release(key):
    '''
    This is the main control function for the app. When buttons get released it goes into here and sees if something needs to happen
    '''
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
            prettyPrintLLM_Messages(aiLists[0].getLLM_Messages())
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


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
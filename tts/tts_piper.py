import subprocess
import re
from constants import piperModelLocation

def generateTTS(text: str, voice: str) -> str:
    '''
    Generates TTS using Piper
    :param text: The text to be converted to speech
    :param voice: The voice to be used for the TTS
    :return: The path to the generated audio file
    '''
    outputPath = "./low.wav"
    sanitizedText = re.sub(r'\[.*\] ', '', text)
    subprocess.run([f"echo", f"{sanitizedText} ", "|", "piper", "--model", f"{piperModelLocation}{voice}", "--output_file", f"{outputPath}"], shell=True, capture_output=True, text=True)
    return outputPath
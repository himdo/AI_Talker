import pyaudio
import wave

class wav_player:
    '''
    This is a class that is used to play audio from a file.
    '''
    def __init__(self):
        self.pa = pyaudio.PyAudio()

    def play_audio(self, file_path: str):
        '''
        This function plays audio from a file.
        :param file_path: The path to the audio file
        '''
        file = wave.open(rf"{file_path}", 'rb')
        chunk = 1024

        self.stream = self.pa.open(format=self.pa.get_format_from_width(file.getsampwidth()),
                                   channels=file.getnchannels(),
                                   rate=file.getframerate(),
                                   output=True)
        
        data = file.readframes(chunk)
        while data:
            self.stream.write(data)
            data=file.readframes(chunk)
        
        self.stream.stop_stream()
        self.stream.close()

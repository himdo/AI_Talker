from colorama import Fore
import pyaudio
import wave
import uuid

class recorder:
    '''
    This is a class that is used to record audio from the microphone.
    '''
    def __init__(self,
                CHUNK = 1024,
                FORMAT = pyaudio.paInt16,
                CHANNELS = 1,
                RATE = 16000):
        self.CHUNK = CHUNK
        self.FORMAT = FORMAT
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.recording = False
        self.pa = pyaudio.PyAudio()
    
    def start(self):
        '''
        This function starts the recording of the microphone.
        '''
        if not self.recording:
            self.filelocation = "./whisper/audio_files/{}.wav".format(uuid.uuid4())
            self.wf = wave.open(self.filelocation, 'wb')
            self.wf.setnchannels(self.CHANNELS)
            self.wf.setsampwidth(self.pa.get_sample_size(self.FORMAT))
            self.wf.setframerate(self.RATE)

            def callback(in_data, frame_count, time_info, status):
                #file write should be able to keep up with audio data stream (about 1378 Kbps)
                self.wf.writeframes(in_data) 
                return (in_data, pyaudio.paContinue)

            self.stream = self.pa.open(format=self.FORMAT,
                                       channels=self.CHANNELS,
                                       rate=self.RATE,
                                       input=True,
                                       frames_per_buffer=self.CHUNK,
                                       stream_callback=callback)
            self.stream.start_stream()
            self.recording = True
            print(f"{Fore.RED}* recording\nPress Space to end recording")

    def stop(self)->str:
        '''
        This function stops the recording of the microphone.
        :return: The file location of the recorded audio
        '''
        if self.recording:
            self.stream.stop_stream()
            self.stream.close()
            self.wf.close()

            self.recording = False
            print(f"{Fore.GREEN}* done recording")
            return self.filelocation

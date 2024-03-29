import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "convertedTowavFile.wav"

paudio = pyaudio.PyAudio()

stream = paudio.open(format = FORMAT, channels = CHANNELS,
		rate = RATE,
		input = True,
		frames_per_buffer = CHUNK)
print(".....Recording Started.....")
arrayFrames=[]
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	data = stream.read(CHUNK)
	arrayFrames.append(data)
print(".....Recording Ended.....")
stream.stop_stream()
stream.close()
paudio.terminate()


waveform = wave.open(WAVE_OUTPUT_FILENAME,'wb')
waveform.setnchannels(CHANNELS)
waveform.setsampwidth(paudio.get_sample_size(FORMAT))
waveform.setframerate(RATE)
waveform.writeframes(b''.join(arrayFrames))
waveform.close()




















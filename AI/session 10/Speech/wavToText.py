import speech_recognition as speechrecog

recog = speechrecog.Recognizer()
audioFile = "convertedTowavFile.wav"

with speechrecog.AudioFile(audioFile) as source:
	audioData = recog.record(source)
	try:
            text = recog.recognize_google(audioData)
            print("Text : "+text)
	except speechrecog.UnknownValueError:
	    print("Google API cannot recognize")
	except speechrecog.RequestError as e:
	    print("Could not request from Google API; {0}".format(e))
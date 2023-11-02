set computerVoice  = CreateObject("SAPI.spvoice")

'This is for Female voice: (Use only one at same time either male voice or female)
'set computerVoice.voice = computerVoice.GetVoices.Item(1)
'This is for the male voice
set computerVoice.voice = computerVoice.GetVoices.Item(0)
computerVoice.speak "Hello Awesome Viewers"
wscript.sleep 500
computerVoice.speak "How are you all?"
wscript.sleep 500
computerVoice.speak "I am computer generated Male voice"
wscript.sleep 500
computerVoice.speak "Welcome to my channel"
wscript.sleep 500
computerVoice.speak "Do you want to know how computer voice replaced Azhar voice"
wscript.sleep 500
computerVoice.speak "Let the real Azhar explain with an example"
wscript.sleep 500
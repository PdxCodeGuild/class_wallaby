# Mini Capstone
# Write blog posts using speech to text, then post online

# Sources:
# https://pypi.org/project/SpeechRecognition/
# https://realpython.com/python-speech-recognition/ 
# https://www.youtube.com/watch?v=x8xjj6cR9Nc&ab_channel=TraversyMedia

'''
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "./chromedriver"
driver = webdriver.Chrome(executable_path = PATH)
driver.get("http://www.python.org") # url?
driver.close()
'''

import speech_recognition as sr

# to use microphone:
# installed portaudio
# install pyaudio: https://pypi.org/project/PyAudio/ https://pypi.org/project/SpeechRecognition/

# from https://www.youtube.com/watch?v=x8xjj6cR9Nc&ab_channel=TraversyMedia
r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I didn\'t get that.')
        except sr.RequestError:
            print('Please try again later.')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Alexis')
    
print('How can I help you?')
voice_data = record_audio()
respond(voice_data)
# print(voice_data)



'''
# tests with audio files - working
test_harvard = sr.AudioFile('audio_files_harvard.wav')
with test_harvard as source:
    audio = r.record(source)
    voice_data1 = r.recognize_google(audio)
    print(voice_data1)

test_jackhammer = sr.AudioFile('audio_files_jackhammer.wav')
with test_jackhammer as source:
    audio = r.record(source)
    voice_data2 = r.recognize_google(audio)
    print()
    print(voice_data2)
'''

# Mini Capstone
# build a program that solves a problem or accomplishes a task
# utilizing an external library

# Sources:
# https://realpython.com/python-speech-recognition/ 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.close()

import speech_recognition

# install portaudio & pyaudio to use microphone: https://pypi.org/project/PyAudio/ https://pypi.org/project/SpeechRecognition/

r = speech_recognition.Recognizer()

test_harvard = speech_recognition.AudioFile('audio_files_harvard.wav')
with test_harvard as source:
    audio = r.record(source)

r.recognize_google(audio)
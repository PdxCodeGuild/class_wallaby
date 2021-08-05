# Mini Capstone
# Write blog posts using speech to text, then post online

# Sources:
# https://pypi.org/project/SpeechRecognition/
# https://realpython.com/python-speech-recognition/ 
# https://www.youtube.com/watch?v=x8xjj6cR9Nc&ab_channel=TraversyMedia
# https://www.guru99.com/reading-and-writing-files-in-python.html#1

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
import random
import time
import playsound
import os
import webbrowser
from gtts import gTTS

# to use microphone:
# installed portaudio
# !!! unable to install pyaudio: https://pypi.org/project/PyAudio/ https://pypi.org/project/SpeechRecognition/

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            assistant_speak(ask)
        audio = r.listen(source)
        voice_command = ''
        try:
            voice_command = r.recognize_google(audio)
        except sr.UnknownValueError:
            assistant_speak('Sorry, I didn\'t get that.')
        except sr.RequestError:
            assistant_speak('Please try again later.')
        return voice_command
    
def assistant_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio' + str(r) + '.wav'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_command):
    if 'new' in voice_command:
        assistant_speak('OK, let\'s record a new blog post.')
        # ask for title
        title = record_audio('What is the title for your blog post?')
        # create file title.txt to capture audio recording
        with open({title}.txt, 'w') as f:
            f.write(f"{title}\n")
            f.close()
        with sr.Microphone() as source:
            audio = r.record(source)
            voice_data = r.recognize_google(audio)
        print(voice_data)
    if 'stop' in voice_command:
        # stop recording
        assistant_speak('Recording stopped.')
        print(voice_data)
        # save audio output to title.txt
        with open({title}.txt, 'w') as f:
            f.write(f"{title}\n")
            f.write(voice_data)
            # f.close()
            assistant_speak(f'File created called {title}.txt')    
    if 'post' in voice_command:
        # open blog
        url = 'https://www.blogger.com/blog/post/edit/5461940182074273538/4621234515163086597?hl=en'
        webbrowser.get().open(url)
        # open title.txt so user can copy & paste, format, & manually hit publish
        # - OR - 
        # transfer text to title & paragraph
        # publish 
    if 'exit' in voice_command:
        exit()
    
time.sleep(1)
assistant_speak('How can I help you? You can say "new," "stop," "post," or "exit."')
while 1:
    voice_command = record_audio()
    respond(voice_command)
    # print(voice_data)
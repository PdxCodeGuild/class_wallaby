# Mini Capstone
# Write blog posts using speech to text, then post online

# Sources:
# https://pypi.org/project/SpeechRecognition/
# https://realpython.com/python-speech-recognition/ 
# https://www.youtube.com/watch?v=x8xjj6cR9Nc&ab_channel=TraversyMedia
# https://towardsdatascience.com/building-a-speech-recognizer-in-python-2dad733949b4
# https://www.geeksforgeeks.org/python-speech-recognition-on-large-audio-files/

'''
from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "./chromedriver"
driver = webdriver.Chrome(executable_path = PATH)
driver.get("http://www.python.org") # url?
driver.close()
'''
# punctuation: grammer checker
'''
import speech_recognition as sr
import random
import time
import playsound
import os
import webbrowser
from gtts import gTTS

r = sr.Recognizer()

def record_audio(command=False):
    with sr.Microphone() as source:
        if command:
            assistant_speak(command)
        audio = r.listen(source)
        voice_command = ''
        try:
            voice_command = r.recognize_google(audio)
        # how to let user control when recording ends?
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

def respond_title(voice_command):
    if 'new' in voice_command:
        assistant_speak('OK, let\'s record a new blog post.')
        # ask for title
        title = record_audio('What is the title for your blog post?')
        # create file title.txt to capture audio recording
        prompt = assistant_speak(f'Do you want to keep {title}?')
        while prompt == 'no':
            assistant_speak('Please speak your new title')
            title = record_audio('What is the title for your blog post?')
            assistant_speak(f'New title is {title}')
            prompt = assistant_speak(f'Do you want to keep {title}?')
        with open(f'{title}.txt', 'w') as f:
            f.write(f"{title}")
            f.close()



def body_respond(voice_command):
    if 'new' in voice_command:
        assistant_speak('OK, let\'s record a new blog post.')
    blog_post = record_audio('Begin speaking. Say end to stop recording.')
    with open(f'{title}.txt', 'w') as f:
        f.write(f'{title}\n\n')
        f.write(blog_post)
        f.close()
    
    # assistant_speak(f'File created called {title}.txt. Say "post" to publish or "exit" to end the program.')
    # run code block to check if user is done speaking
    while ...

    assistant_speak('Are you done recording?')
    if assistant_speak == 'no':
        print(body_respond(voice_command)) 

        
    if 'end' in voice_command:
        # how to end recording?
        assistant_speak('Recording ended.')
        assistant_speak(f'File created called {title}.txt. Say "post" to publish or "exit" to end the program.')
        # how to open the program?
        
    if 'post' in voice_command:
        # https://console.cloud.google.com/apis/credentials?project=thinking-avenue-322101&supportedpurview=project
        # # open blog publisher
        url = 'https://www.blogger.com/blog/post/edit/5461940182074273538/4621234515163086597?hl=en'
        webbrowser.get().open(url)
        # open title.txt so user can copy & paste, format, & manually hit publish
        # - OR - 
        # transfer text to title & paragraph
        # publish 
 
    if 'exit' in voice_command:
        exit()


    
time.sleep(1)
assistant_speak('I am here to help. Say "new" to create a new blog post or "exit" to end the program.')
while 1:
    voice_command = record_audio()
    respond(voice_command)

'''
import speech_recognition as sr
import random
import time
import playsound
import os
import webbrowser
from gtts import gTTS


r = sr.Recognizer()

def record_audio(command=False):
    with sr.Microphone() as source:
        if command:
            assistant_speak(command)
        audio = r.listen(source)
        voice_command = ''
        try:
            voice_command = r.recognize_google(audio)
        # how to let user control when recording ends?
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
    #if sr.UnknownValueError:
        # how to handle unknown input? 
        #respond(voice_command)
    
    if 'new' in voice_command:
        assistant_speak('OK, let\'s record a new blog post.')
        # ask for title
        title = record_audio('What is the title for your blog post?')
        # create file title.txt to capture audio recording
        assistant_speak(f'Title is {title}.')
        prompt = record_audio(f'Would you like to re-record title?')
        while prompt == 'yes':
            title = record_audio('What is the title for your blog post?')
            assistant_speak(f'New title is {title}')
            prompt = record_audio(f'Would you like to re-record title?')        
        with open(f'{title}.txt', 'w') as f:
            f.write(f"{title}")
            f.close()    
        blog_post = record_audio('Begin speaking to record your blog post.') # 'Say end to stop recording.'
        # with open(f'{title}.txt', 'w') as f:
        with open(f'{title}.txt', 'a') as f:
            # f.write(f'{title}\n\n')
            f.write(blog_post)
            f.close()
        assistant_speak(f'File created called {title}.txt. Say "post" to publish or "exit" to end the program.')
   
    # if 'end' in voice_command:
        # how to end recording?
        # assistant_speak('Recording ended.')
        # assistant_speak(f'File created called {title}.txt. Say "post" to publish or "exit" to end the program.')
        # how to open the file?
        
    if 'post' in voice_command:
        # https://console.cloud.google.com/apis/credentials?project=thinking-avenue-322101&supportedpurview=project
        # # open blog publisher
        url = 'https://www.blogger.com/blog/post/edit/5461940182074273538/4621234515163086597?hl=en'
        webbrowser.get().open(url)
        # open title.txt so user can copy & paste, format, & manually hit publish
        # with open(f'{title}.txt', 'r'): # error
            # print(f.read(blog_post))
        # - OR - 
        # transfer text to title & paragraph, publish 
        exit()
 
    if 'exit' in voice_command:
        exit()

    # elif sr.UnknownValueError:
        # ?

time.sleep(1)
assistant_speak('I am here to help. Say "new" to begin a new blog post or "exit" to end the program.')
while 1:
    voice_command = record_audio()
    respond(voice_command)
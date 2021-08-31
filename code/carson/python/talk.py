import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
  
while True:    
    engine = pyttsx3.init()
    print("welcome to the parrot app !")
    word = input('What do you want me to say?  : ')     
    print(word)
    if word == "done":
        break   
    else:
        engine.say(word) 
        engine.runAndWait()  
       
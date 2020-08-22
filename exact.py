import pyttsx3
import os
import speech_recognition as SRG
import time
engine=pyttsx3.init()
print('Hello sir, I am your personalized bot.')
pyttsx3.speak('Hello sir I am your personalized bot')
print('Welcome to my world.')
pyttsx3.speak('Welcome to my world')

while True:
    variable = SRG.Recognizer()
    with SRG.Microphone() as source:
        print('How may I help you?')
        engine.runAndWait()
        
        audio_input = variable.record(source,duration=6)
        try:
            text = variable.recognize_google(audio_input)
            print(text)
        except:
            print('Could not process audio...')
            pyttsx3.speak('Could not process audio')
            break
    if ('can' in text) and ('do' in text) and ('for' in text) and ('me' in text) and ('you' in text):
        print('I can open chrome for you.')
        pyttsx3.speak('I can open chrome for you.')
        print('I can open linkedin for you.')
        pyttsx3.speak('I can open linkedin for you.')
        print('I can open facebook for you.')
        pyttsx3.speak('I can open facebook for you.')
        print('I can open calculator for you.')
        pyttsx3.speak('I can open calculator for you.')
        print('I can open notepad for you.')
        pyttsx3.speak('I can open notepad for you.')
        print('I can open media player for you.')
        pyttsx3.speak('I can open media player for you.')
        print('I can open Youtube for you.')
        pyttsx3.speak('I can open youtube for you.')
        print('I can play songs for you.')
        pyttsx3.speak('I can play songs for you.')
    elif (('open' in text) or ('Open' in text)) and (('chrome' in text) or ('Chrome' in text)):
        pyttsx3.speak('Opening Chrome')
        os.system('start chrome')
        
    elif (('open' in text) or ('Open' in text)) and ('LinkedIn' in text):
        pyttsx3.speak('Opening Linkedin')
        os.system('start chrome https://www.linkedin.com/feed/')
        
    elif (('Open' in text) or ('open' in text)) and (('Facebook' in text) or ('facebook' in text)):
        pyttsx3.speak('Opening Facebook')
        os.system('start chrome https://www.facebook.com/')
    elif (('open' in text) or ('Open' in text)) and ('YouTube' in text):
        pyttsx3.speak('Opening Youtube')
        os.system('start chrome https://www.youtube.com/')
    elif (('play' in text) or ('Play' in text)) and ('song' in text):
        pyttsx3.speak('Playing Song')
        os.system('start chrome https://gaana.com/playlist/sksujauddin2ganacomsongs')
        

        
    elif (("open" in text) or  ("execute" in text ) or ('Open' in text) ) and  (("notepad" in text) or ("editor" in text) or ('Notepad' in text)):
        pyttsx3.speak('Opening notepad')
        os.system("start notepad")
        
    elif (("open" in text) or ('Open' in text)) and ("player" in text) and ("media" in text):
        pyttsx3.speak('Opening media player')
        os.system('start wmplayer')
        
    elif (("open" in text) or  ("execute" in text ) or ('Open' in text) ) and (("calculator" in text) or ('Calculator' in text)):
        pyttsx3.speak('Opening calculator')
        os.system('calc')
        
    elif ("exit" in text)  or ("quit" in text) or ('Exit' in text) or ('Quit' in text):
        print('Bye Bye, have a nice day!!')
        pyttsx3.speak('Bye Bye Have a nice day')
        break
    else:
        print("command does not support")
        pyttsx3.speak('Command does not support')
        
    
        
    

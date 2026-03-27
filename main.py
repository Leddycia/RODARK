import datetime
import json  # json-   json-

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import weathercom
import wikipedia
import sys
import action as a

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
engine.say('Awake')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global cmd
    try:
        with sr.Microphone() as source:
            print('Clear background noises...')
            # Ajuste le niveau du micro par rapport au bruit ambiant
            listener.adjust_for_ambient_noise(source, duration=1)
            print('ok')
            talk('What can I do for you')
            listener.pause_threshold = 0.5

            # Écoute la voix
            voice = listener.listen(source)

            # Demande à Google de transcrire (par défaut en anglais)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()

    except sr.UnknownValueError:
        # Google n'a pas compris l'audio (bruit, silence, ou mauvaise prononciation)
        print("Audio non reconnu.")
        cmd = ""  # On vide la commande pour que le programme ne plante pas

    except sr.RequestError:
        # Problème de connexion internet
        print("Erreur de connexion avec les serveurs.")
        cmd = ""


def execute_Rodark():
    take_command()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        talk('playing' + song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'tell me the time' in cmd:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        talk('Current time is' + current_time)

    elif 'who is' in cmd:
        person = cmd.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in cmd:
        thing = cmd.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)

    elif 'joke' in cmd:
        talk(pyjokes.get_jokes())
        if len('joke') < 2:
            sys.exit('Stop')

    elif 'Taken' in cmd:
        talk('yes, i have a girldfriend')

    elif 'How are you' in cmd:
        talk('Fine, thanks')

    elif 'tell me your name' in cmd:
        talk('I am Rodark, a virtual assistant. I am currently in construction so i make some mistakes time to time')

    elif 'pretty' in cmd:
        talk('You are the prettiest girl in the world')

    elif 'beautiful' in cmd:
        talk('Yes, you are')

    elif 'ugly' in cmd:
        talk('No, you are pretty')

    elif 'Do you think you are funny' in cmd:
        talk('No, i am not funny')

    elif 'hi' in cmd:
        talk('hi')

    elif 'hello' in cmd:
        talk('hello')

    elif 'good morning' in cmd:
        talk('Good morning')

    elif 'good afternoon' in cmd:
        talk('Good afternoon')

    else:
        talk('May you repeat please')


def weatherReport(city):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weatherDetails)['vt1observation']['humidity']
    temp = json.loads(weatherDetails)['vt1observation']['temperature']
    phrase = json.loads(weatherDetails)['vt1observation']['phrase']
    return humidity, temp, phrase


while True:
    execute_Rodark()

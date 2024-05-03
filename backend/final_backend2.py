import pyttsx3
import pywhatkit
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import ctypes
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def query_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{time[1]}O'clock and {time[3:5]} minutes") 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !") 

    else:
        speak("Good Evening Sir !") 

    assname =("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)
    

def username():
    speak("What should i call you ")
    uname = takeCommand()
    speak("Welcome master")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    print("#####################".center(columns))
    print("Welcome master", uname.center(columns))
    print("#####################".center(columns))
    
    speak("How can i Help you today")

def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) 
        print("Unable to Recognize your voice.") 
        return "None"
    
    return query



if __name__ == '__main__':
    clear = lambda: os.system('cls')
    assname =("Baymax")
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
    
    while True:
        
        query = takeCommand().lower()
        
        # All the commands said by user will be 
        # stored here in 'query' and will be
        # converted to lower case for easily 
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com/")


        elif 'open Instagram' in query:
            speak("Here you go to Instagram\n")
            webbrowser.open("https://www.instagram.com/")
        
        
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.com/")

        

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = r"C:\Users\Tushar Kulkarni\Music"                       #change dir
            songs = os.listdir(music_dir)
            print(songs) 
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            query_time()
        
            
        elif 'open brave' in query:
            codePath = r"C:\Users\Tushar Kulkarni\AppData\Local\Programs\Opera GX\launcher.exe"#directory change
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"#directory change
            os.startfile(codePath)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif "calculator" in query: 
            
            codePath = r"C:\Windows\System32\calc.exe"              #directory change
            os.startfile(codePath)


        elif 'search' in query or 'play' in query:
            
            query = query.replace("search", "") 
            query = query.replace("play", "")		 
            webbrowser.open(query) 

        elif "who am i" in query:
            speak("you are my master")
            

        elif "why you came to this world" in query:
            speak("Thanks to a human. further It's a secret")

        elif 'powerpoint ' in query:
            speak("opening Power Point presentation")
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"             #directory change 
            os.startfile(power)

        elif 'Word file' in query:
            speak("opening word file")
            word = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"               #directory change 
            os.startfile(word)


        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")



        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                    0, 
                                                    "Location of wallpaper",
                                                    0)
            speak("Background changed successfully")

        elif 'news' in query:
            
            try: 
                jsonObj = urlopen("https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=e04e172367d94da282f92dc22604a3c8")
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                
                print(str(e))

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            file.write(note)
        
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))             
        
        elif "jarvis" in query:
            speak("Jarvis 1 point o in your service Mister")
        
        elif "search web " in query:
            pywhatkit.search(query)
            speak('This is what I found')
        
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        
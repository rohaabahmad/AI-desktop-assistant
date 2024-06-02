import pyttsx3        #  text-to-speech conversion, It allows the script to generate speech output.
import requests        #  for fetching data from web servers.
import speech_recognition as sr    # to recognize speech from audio input.
import datetime   #  provides classes for manipulating dates and times. It's used here to get the current time.
import wikipedia  # provides access to the Wikipedia API
import webbrowser  #  allows the script to open web pages in the default web browser.
import os   # provides a portable way of using operating system-dependent functionality
import feedparser  # allows the script to fetch and parse news headlines from RSS feeds
import pywhatkit as wk   # provides various utilities for working with WhatsApp and web-related tasks
import random  #  provides functions for generating random numbers
import pyautogui # provides cross-platform support for controlling the mouse and keyboard
import time  # provides various time-related functions
from bs4 import BeautifulSoup  # commonly used in web scraping to extract data from web pages


#  initializing the text-to-speech engine using pyttsx3 library. 
#  It sets the voice property to the first voice available on the system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function taking string audio as input

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# This function greets the user based on the time of the day and introduces the voice assistant

def wishMe():
    hour = datetime.datetime.now().hour
    speak("ASSALAMO-ALAIKUM")
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Your desktop voice assistant Sir. Please tell me how may I help you")

#  This function listens to the microphone input and converts it into text using the Google Speech Recognition API

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("say that again please ...")
        return "None"
    return query




def getNews():
    # Example: Fetch news from BBC News RSS feed
    
    url = 'http://feeds.bbci.co.uk/news/rss.xml'
    feed = feedparser.parse(url)
    news = feed.entries
    for i in range(5):  # Display top 5 news headlines
        speak(news[i].title)

# it is the entry point of the program. It initializes the assistant, listens for user commands, and executes the corresponding actions based on the commands given

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'stop' in query:
            speak("stopping the assistant..")
            break

        if 'wikipedia' in query:
          speak('Searching Wikipedia...')

          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)



        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            

        elif 'watch youtube' in query:
            webbrowser.open("youtube.com")
            speak("What would you like to watch ?")
            query = takeCommand().lower()
            wk.playonyt(f"{query}")


        elif 'search on youtube' in query:
            query=query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'search google' in query:
            speak("what should I search ?")
            query = takeCommand().lower()
            webbrowser.open(f"{query}")
            results = wikipedia.summary(query, sentences=1)
            speak(results)


        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\MOIZ\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\MOIZ\\Desktop\\JARVIS AI\\JAI.PY"
            os.startfile(codePath)


        elif 'news' in query:
            getNews()


        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")


        elif 'take screenshot' in query:
            speak("tell me a name of file to be saved")
            name=takeCommand().lower()
            print(f"User said: {name}\n")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")


        elif 'open paint' in query:
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\paint")


        elif 'draw a line' in query:
            
            pyautogui.moveTo(x=400, y=300, duration=1)
            pyautogui.leftClick
            pyautogui.dragRel(400, 0, 1)
            

        elif 'undo' in query:
            pyautogui.hotkey('ctrl', 'z')

        

        elif "temperature" in query:
            speak("plz tell the name of city . .")
            city = takeCommand().lower()
            search =f"temperature in {city}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
            print(f"current{search} is {temp}")


    
            



from tempfile import TemporaryFile
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("A very Good Morning Sir, Edith at your service")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir, Edith at your service")
    else:
        speak("Good evening sir, Edith at your service")
    speak("How may i help you today")

# It takes microphone input from the user and return string output

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print('Listening... ')
         r.pause_threshold = 0.5
         r.energy_threshold = 450
         audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query






if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

# Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        elif 'open gmail' in query:
            webbrowser.open(" mail.gmail.com")
        elif 'open insta' in query:
            webbrowser.open("instagram.com")


        elif 'play music' in query:
            music = 'D:\\music'
            songs= os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[1]))


        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'quit' in query:
            exit()




        
        
          
        







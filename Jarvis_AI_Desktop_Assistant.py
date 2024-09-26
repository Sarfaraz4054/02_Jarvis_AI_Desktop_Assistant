import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib
import pywhatkit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")    
    else:
        speak("Good Evening!")
    speak("I am Jarvis.Please tell me how may I help you") 
        
 #It takes microphone input from the user and return string output
def takeCommand():   
    r=sr.Recognizer()
    with sr.Microphone() as source: 
       print("Listening...") 
       r.pause_threshold = 1
       audio = r.listen(source)
    try:
        print("Recognizing...") 
        query=r.recognize_google(audio,language='en-in')  
        print(f"user said:{query}\n")  
    except Exception as e:
        print(e)  
        print("Say that again please...")       
        return "None"   
    return query
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sonuhyd0@gmail.com','ikalnjlxscgnypnz')
    server.sendmail('sonuhyd0@gmail.com', to, content)
    server.close()
    
if __name__=="__main__":
    wishMe()
    # if 1:
    while True:
        query=takeCommand().lower()  
  
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google'  in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")     
        elif 'play music'  in query:
            music_dir='D:\\Non Critical\\songs\\Fovarite songs2'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"Sir,the time is {strTime}") 
        elif 'play' in query and 'on youtube' in query:
             song = query.replace('play', '').replace('on youtube', '')
             speak(f"Playing {song} on YouTube")
             pywhatkit.playonyt(song)    
        elif 'open vs code' in query:  
            codePath="C:\\Users\\sarfaraz ahmed\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)        
        elif 'email to sonu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sonuhyd0@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 
        elif 'open email' in query:
            speak("Opening your email")
            webbrowser.open("https://mail.google.com")
        elif 'power off' in query:
            speak("see you soon friend")
            os.system("shutdown /s /t 1")    
                
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
from voice_password import password  # Import the password from the separate file

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)  
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")    
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():   
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')  
        print(f"user said: {query}\n")  
    except Exception as e:
        print(e)  
        print("Say that again please...")       
        return "None"   
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sonuhyd0@gmail.com', 'vwddtlwcclbtjupr')  # Use app password or proper security method
    server.sendmail('sonuhyd0@gmail.com', to, content)
    server.close()

# List of pre-selected email addresses
email_list = ["thisvilen@gmail.com", "sonuhyd0@gmail.com", "kunukuntlakasyap@gmail.com", "21ve1a6628@sreyas.ac.in", "ironmantony890@gmail.com"]

# Function to schedule the meeting for tomorrow
def scheduleMeeting():
    try:
        # Get the current date and calculate tomorrow's date
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        
        subject = f"Scheduled Meeting for {tomorrow.strftime('%A, %B %d, %Y')}"
        body = f"This is a reminder for the meeting scheduled for {tomorrow.strftime('%A, %B %d, %Y')} at 10:00 AM."
        content = f"Subject: {subject}\n\n{body}"
        
        # Send email to each pre-selected email
        for email in email_list:
            sendEmail(email, content)
        speak(f"Meeting scheduled for {tomorrow.strftime('%A, %B %d, %Y')} successfully and emails sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am unable to schedule the meeting.")

def verifyPassword():
    speak("Please speak your password to continue")
    user_password = takeCommand().lower()  # Convert user voice input to lower case for comparison
    if user_password == password:
        speak("Password matched. You may proceed.")
        return True
    else:
        speak("Password did not match. You are not authorized.")
        return False

if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()  
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"Sir, the time is {strTime}")

        elif 'play' in query and 'on youtube' in query:
            song = query.replace('play', '').replace('on youtube', '')
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        elif 'open vs code' in query:  
            codePath = "C:\\Users\\sarfaraz ahmed\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)        

        elif 'email to sonu' in query:
            speak("You are trying to send an email. Password verification required.")
            
            if verifyPassword():
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "sonuhyd0@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")
            else:
                speak("Email sending operation aborted due to incorrect password.")

        elif 'open email and schedule a meeting for tomorrow' in query:
            speak("You are trying to open the email and schedule a meeting. Password verification required.")
    
            if verifyPassword():  # Verify password before proceeding
              speak("Opening your email and scheduling a meeting for tomorrow.")
              webbrowser.open("https://mail.google.com")
              scheduleMeeting()
            else:
                speak("Operation aborted due to incorrect password.")
 

        elif 'open email' in query:
            speak("You are trying to open the email. Password verification required.")
    
            if verifyPassword():  # Verify password before opening the email
               speak("Opening your email")
               webbrowser.open("https://mail.google.com")
            else:
                speak("Email opening operation aborted due to incorrect password.")

        elif 'power off' in query:
            speak("See you soon friend")
            os.system("shutdown /s /t 1")



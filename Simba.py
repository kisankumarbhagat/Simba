import pyttsx3
import speech_recognition as sr 
import datetime
from datetime import timedelta
import wikipedia 
import webbrowser
import os
import pyjokes
import pywhatkit
import wolframalpha
import screen_brightness_control as sbc
from ctypes import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" Hi!. I am Simba. How can  I  Help You")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print (audio)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

#def sendEmail(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('youremail@gmail.com', 'your-password')
    #server.sendmail('youremail@gmail.com', to, content)
    #server.close()


if _name_ == "_main_":
    wishMe()
   
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            print("Opening YouTube")
            speak('Opening YouTube')
            speak("what do you want to search on youtube")
            search1=takeCommand().lower()
            search1 = search1.replace("on youtube", "")
            pywhatkit.playonyt(search1)
        

        elif 'google' in query:
            speak("what do you want to search on google")
            search1=takeCommand().lower()
            search1 = search1.replace("on google", "")
            try:
                pywhatkit.search(search1)
                print("Searching...")
            except:
                print("An unknown error occurred")

        
            
        elif 'whatsapp' in query:
            speak("To whome You want to massage")
            search2=takeCommand().lower()
            if "Contact_1" in search2:
                speak("What massage you want to send")
                search3=takeCommand()
                search3=search3.replace("send","")
                
                hour = int(datetime.datetime.now().hour)
                mint= int(datetime.datetime.now().minute)
                pywhatkit.sendwhatmsg('Contact_No.', search3,hour,mint+1)
            elif "Contact_2" in search2:
                speak("What massage you want to send")
                search3=takeCommand()
                search3=search3.replace("send","")
                hour = int(datetime.datetime.now().hour)
                mint= int(datetime.datetime.now().minute)
                pywhatkit.sendwhatmsg('Contact_No.', search3,hour,mint+1)
            elif "Contact_3" in search2:
                speak("What massage you want to send")
                search3=takeCommand()
                search3=search3.replace("send","")
                hour = int(datetime.datetime.now().hour)
                mint= int(datetime.datetime.now().minute)
                pywhatkit.sendwhatmsg('Contact_No.', search3,hour,mint+1 )

          


        elif 'play movie' in query:
            music_dir = 'D:\\MOVIE\\Dahan (2022) Hindi 720p WEBRip x264 AAC ESub'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play music' in query:
            music_dir = "D:\songs"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by ....")

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'open vs code' in query:
            codePath = (r"C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
            os.startfile(codePath)

        
        elif "brightness" in query:
            if "increase" in query:
                monitors = sbc.list_monitors()
                print(monitors)
                sbc.set_brightness(90, display=monitors[0])
            else:
                monitors = sbc.list_monitors()
                print(monitors)
                sbc.set_brightness(25, display=monitors[0])
        
        elif "shut down" in query:
            speak("Do you wish to shutdown your computer ? (yes / no): ")
            shutdown=takeCommand()
            if shutdown == 'no':
                exit()
            else:os.system("shutdown /s /t 1")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif "what is" in query or "who is" or "when" not in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client('WolframAlpha_API')
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
                
                        

            except:
                speak(""+query+"!!! would you like me to search this on google")
                command= takeCommand() 
                if 'yes'in command:
                    pywhatkit.search(query)
                else :StopIteration:print ("No results")

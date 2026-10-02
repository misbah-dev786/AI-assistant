import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import requests
import pc_control
from ai_chat import ask_Ai

def speak (text):
    Engine = pyttsx3.init()
    Engine.setProperty("volume",1.8)
    Engine.setProperty("rate",190)
    Engine.say(text)
    Engine.runAndWait()

def process(command):
    
    # app controll
    if "open youtube" in command:
         print("you said : ",command)
         webbrowser.open("https://www.youtube.com")
         
    elif "open google" in command:
        print("you said : ",command)
        webbrowser.open("https://www.google.com")
        
    elif "open firefox" in command:
        print("you said : ",command)
        webbrowser.open("https://www.firefox.com")
    
    elif "open microsoft" in command:
        webbrowser.open("https://www.microsoftedge.com")
        
    elif "open wattsapp" in command :
        pc_control.open_wattsapp()
        
    elif "open chatbot" in command:
        pc_control.open_chatbot()
        
    # yotube search sytem 
    elif command.startswith("play"):
        search = command[5:].strip()
        print("you said : ",command)
        pywhatkit.playonyt(search)
        
    # folder controll 
    elif "open" in command and "mycomputer" in command:
        pc_control.open_myComputer
        
    elif "open" in command and "loads" in command:
        pc_control.open_downloads()
           
    elif "open" in command and "documents" in command:
        pc_control.open_documents()
      
    elif "open" in command and "pictures" in command:
        pc_control.open_pictures()
        
    elif "open" in command and "music" in command:
        pc_control.open_music()
            
    elif "open" in command and "videos" in command:
        pc_control.open_videos()
       
    elif "open" in command and "calculator" in command:
        pc_control.open_caculator()
        
    # sytem controll
    elif "restart mycomputer" in command :
        print("pc restarting in 10 seconds!")
        pc_control.restart()
    
    elif "shuttdown mycomputer" in command:
        print("pc shutting down in 10 seconds!")
        pc_control.shutdown()
        
    elif "sleep mycomputer" in command:
        pc_control.sleep()
        
    elif "cancel shuttingdown" in command:
        print("shutting cancel")
        pc_control.cancel_shutdown()
    
    # for AI responces        
    else :
        responce = ask_Ai(command)
        speak(responce)
               
if __name__ == "__main__":
    speak("programm is started.....")
    while(True):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        
        print("listening....")
        try:
            with mic as source:
                audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            
            if(command.lower() == "alex"):
                speak("yes i am listening")
                
                with mic as source:
                    print("alex is active")
                    print("listening...")
                    recognizer.adjust_for_ambient_noise(source,duration=1)
                    audio = recognizer.listen(source,timeout=2,phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    command = command.lower()   
                    process (command)            
        except Exception as e:
            print("error{0}".format(e)) 
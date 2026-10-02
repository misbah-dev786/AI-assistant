import os
import subprocess

# folders control
def open_myComputer():
    os.startfile(r"C:\Users\your name\Desktop\This PC - Shortcut.lnk")
    
def open_downloads():
    os.startfile(r"C:\Users\your name\Downloads")

def open_documents():
    os.startfile(r"C:\Users\your name\Documents")

def open_pictures():
    os.startfile(r"C:\Users\your name\Pictures")

def open_videos():
    os.startfile(r"C:\Users\your name\Videos")
    
def open_music():
    os.startfile(r"C:\Users\your name\Music")

# apps control
def open_caculator():
    os.startfile(r"C:\Users\your name\Desktop\Calculator.lnk")
    
def open_wattsapp():
    os.startfile(r"C:\Users\your name\Desktop\WhatsApp.lnk")
    
def open_chatbot():
    os.startfile(r"C:\Users\your name\Desktop\ChatGPT Classic.lnk")

def open_playit():
    os.startfile(r"C:\Users\your name\Desktop\PLAYit.lnk")
    
# system control
def restart():
    os.system("restart /r /t 10")
    
def shutdown():
    os.system("shutdown /s /t 10")
    
def cancel_shutdown():
    os.system("shutdown /a")
      
def sleep():
    subprocess.run("rund1132.exe powrprof.dll,setSuspendState 0,1,0")
    
    
    
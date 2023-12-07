#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install pyttsx3


# In[13]:


pip install SpeechRecognition


# In[18]:


pip install pyjokes


# In[22]:


pip install PyAudio


# In[144]:


import pyttsx3 #convert text into speech
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptxt():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try: 
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")
#sptxt()
            

def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)   #0 for male voice
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)   #for speed of voice
    engine.say(x)
    engine.runAndWait()
    
#speechtx("hello guys! This is my voice assistant project")



if __name__=='__main__':
    
    #if sptxt().lower()=="hey tweety":
    while True:
        data1=sptxt().lower()
        if "your name" in data1:
            name="my name is tweety"
            speechtx(name)
        
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "python page" in data1:
            webbrowser.open("https://pypi.org/")
        elif "joke" in data1:
            joke1=pyjokes.get_joke(language="en",category="neutral")
            print(joke1)
            speechtx(joke1)
        elif "exit" in data1:
            speechtx("Thank you")
            print("Thank you")
            break
            
    
  
              


# In[ ]:





# In[ ]:




